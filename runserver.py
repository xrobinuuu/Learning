import argparse
import configparser
import os
import pathlib
import sys

import uvicorn


class StartServer:
    host: str = "0.0.0.0"
    port: int = 8000

    @classmethod
    def _load_server_config(cls):
        host = os.environ.get("SERVER_HOST")
        port = os.environ.get("SERVER_PORT")
        config_path = pathlib.Path(__file__).resolve().parent.parent.joinpath("config.ini")
        if config_path.exists():
            encoding = 'utf-8-sig' if sys.platform.lower() in ['win32'] else 'utf-8'
            config_parser = configparser.ConfigParser()
            config_parser.read(config_path, encoding=encoding)
            if "server" in config_parser:
                if host is None and "host" in config_parser["server"]:
                    host = config_parser.get("server", "host")
                if port is None and "port" in config_parser["server"]:
                    port = config_parser.get("server", "port")
        if host is not None:
            cls.host = host
        if port is not None:
            cls.port = int(port)

    @classmethod
    def run(cls):
        cls._load_server_config()
        parser = argparse.ArgumentParser(description="START API SERVER")
        parser.add_argument("--host", "-H", type=str, default=cls.host, help=f"default: {cls.host}")
        parser.add_argument("--port", "-P", type=int, default=cls.port, help=f"default: {cls.port}")
        parser.add_argument("--reload", type=bool, default=False, help="default: False")
        parser.add_argument("--workers", type=int, default=1, help="default: 1")
        args = parser.parse_args()
        app = f"{pathlib.Path(__file__).resolve().parent.name}.app_router:app"
        sys.path.insert(0, pathlib.Path(__file__).resolve().parent.parent.as_posix())
        uvicorn.run(app=app, host=args.host, port=args.port, reload=args.reload, workers=args.workers)


if __name__ == '__main__':
    StartServer.run()
