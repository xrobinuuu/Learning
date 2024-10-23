from config.core import LogConfiger
import logging

LogConfiger._config()
logger = logging.getLogger('debug')

logger.debug('dasdasdasd')