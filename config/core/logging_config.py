import logging.config
from pathlib import Path

from colorama import Fore, Style

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PathType = Path | str


class Formatter(logging.Formatter):
    COLOR_MAP = {
        'DEBUG': Fore.WHITE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.LIGHTRED_EX
    }

    def format(self, record: logging.LogRecord):
        fmt = self._fmt.replace('%(lineno)d', '%(lineno)s').replace('%(process)d', '%(process)s')
        self._colorize_record(record)
        return fmt % {**record.__dict__}

    def _colorize_record(self, record: logging.LogRecord):
        levelname = message = self.COLOR_MAP[record.levelname]

        record.asctime = Fore.CYAN + self.formatTime(record) + Style.RESET_ALL
        record.filename = Fore.LIGHTMAGENTA_EX + record.filename + Style.RESET_ALL
        record.module = Fore.LIGHTYELLOW_EX + record.module + Style.RESET_ALL
        record.funcName = Fore.LIGHTGREEN_EX + record.funcName + Style.RESET_ALL
        record.lineno = Fore.BLUE + str(record.lineno) + Style.RESET_ALL
        record.threadName = Fore.LIGHTBLUE_EX + record.threadName + Style.RESET_ALL
        record.process = Fore.LIGHTWHITE_EX + str(record.process) + Style.RESET_ALL
        record.name = Fore.LIGHTWHITE_EX + record.name + Style.RESET_ALL
        record.levelname = levelname + record.levelname + Style.RESET_ALL
        record.message = message + record.getMessage() + Style.RESET_ALL


class Configer:
    SMTP_SETTING = {
        "mailhost": ("smtp.example.com", 587),
        "fromaddr": "your_email@example.com",
        "credentials": ("your_email@example.com", "your_password"),
        "toaddrs": ["recipient@example.com"],
        "subject": "Application Error",
        "secure": ()
    }
    ORIGIN_FMT = "%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s"
    DATE_FMT = "%Y-%m-%d %H:%M:%S"

    config_yaml = Path(__file__).parent.joinpath("logging.yaml")
    logdir = BASE_DIR.joinpath("logs")
    logfile = logdir.joinpath("logging.log")

    def __init__(
            self,
            config_yaml: PathType = config_yaml,
            logfile: PathType = logfile,
            logdir: PathType = logdir,
            _yaml: bool = False,
    ):
        self.logfile = logfile
        self.logdir = logdir
        self._yaml = _yaml

        self.config_yaml = config_yaml
        self._make_logs_dir()

    def config(self):
        if self._yaml:
            log_config = self._read_config_file()
        else:
            log_config = self._init_config_dict()
        logging.config.dictConfig(log_config)

    def init_config_yaml(self):
        import yaml
        log_config = self._init_config_dict()
        with open(self.config_yaml, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(
                log_config,
                yaml_file,
                allow_unicode=True,
                default_flow_style=False
            )

    def _read_config_file(self):
        import yaml
        with open(self.config_yaml, 'r', encoding='utf-8') as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.FullLoader)

    def _make_logs_dir(self):
        self.logdir.mkdir(parents=True, exist_ok=True)

    def _init_config_dict(self):
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": self.ORIGIN_FMT,
                    "datefmt": self.DATE_FMT,
                },
                "colored": {
                    '()': Formatter,
                    "format": self.ORIGIN_FMT,
                    "datefmt": self.DATE_FMT,
                },
            },
            "handlers": {
                "file_handler": {
                    "level": "INFO",
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": self.logfile.as_posix(),
                    "maxBytes": 1024 * 1024 * 5,
                    "backupCount": 5,
                    "encoding": "utf8",
                },
                "terminal": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "colored",
                },
                "email_handler": {
                    "level": "ERROR",
                    "class": "logging.handlers.SMTPHandler",
                    "formatter": "default",
                    **self.SMTP_SETTING
                },
            },
            "loggers": {
                "": {
                    "handlers": ["terminal", "file_handler"],
                    "level": "INFO",
                    "propagate": False,
                },
                "debug": {
                    "handlers": ["terminal"],
                    "level": "INFO",
                    "propagate": False,
                },
            },
        }
