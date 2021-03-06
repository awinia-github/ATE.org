""" Doc """
import json
import os
from ATE.apps.common.logger import Logger


class ConfigReader:

    """Docstring for ConfigReader. """

    def __init__(self, config_file):
        self.host = None
        self.port = None
        self.config_file = config_file
        self.log = Logger.get_logger()

    def get_configuration(self):
        return self.load_json_from_file(self.config_file)

    def get_configuration_ex(self, *, user_config_file: str = None, user_config_dict: dict = None):
        if self.config_file is not None:
            config = self.get_configuration()
        else:
            config = {}

        if user_config_file is not None:
            user_config = self.load_json_from_file(user_config_file)
            config.update(user_config)

        if user_config_dict is not None:
            config.update(user_config_dict)

        return config

    def load_json_from_file(self, json_file_path):
        if not os.path.exists(json_file_path):
            self.log.error(f"configuration file not found: {json_file_path}")

        with open(json_file_path) as f:
            return json.load(f)
