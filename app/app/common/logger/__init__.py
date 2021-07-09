import os
import re
from logging import Logger as SuperLogger, INFO, Formatter
from threading import Thread
from xy.decorator.singleton import Singleton
from ...config import AppConfig
from .handler import RayUserTimedRotatingFileHandler


@Singleton
class Logger(SuperLogger):
    def __init__(self):
        super().__init__("ray-user", INFO)
        log_path = os.path.join(os.path.dirname(AppConfig().app_path), "log")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        log_file_path = os.path.join(log_path, "ray-user")
        timed_rotating_file_handler = RayUserTimedRotatingFileHandler(filename=log_file_path, when="s", interval=1, backupCount=365, encoding="utf-8")
        timed_rotating_file_handler.suffix = "%Y-%m-%d.log"
        timed_rotating_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}(\.\w+)?$")
        timed_rotating_file_handler.setFormatter(formatter)
        self.addHandler(timed_rotating_file_handler)


