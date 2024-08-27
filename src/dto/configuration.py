import json
from typing import List

from flask import current_app


class ProviderConfiguration:
    type: str
    url: str
    email: str
    token: str


class Configuration:
    providers: List[ProviderConfiguration]

    def __init__(self, config_file_path) -> None:
        with open(config_file_path) as f:
            config = json.load(f)
            for key in config:
                setattr(self, key, config[key])

    @staticmethod
    def get() -> "Configuration":
        with current_app.app_context():
            return current_app.config["application"]
