import json
from dataclasses import dataclass

from dacite import from_dict, Config
from flask import current_app

from src.entities.provider_configuration import ProviderConfiguration
from src.enums.provider_type import ProviderType


@dataclass
class Configuration:
    providers: list[ProviderConfiguration]

    @staticmethod
    def get() -> "Configuration":
        with current_app.app_context():
            return current_app.config["application"]

    @staticmethod
    def create(file_path: str) -> "Configuration":
        with open(file_path, encoding="utf-8") as f:
            config = json.load(f)
            return Configuration._create_from_dict(config)

    @staticmethod
    def _create_from_dict(configuration_dict: dict):
        return from_dict(
            data_class=Configuration,
            data=configuration_dict,
            config=Config(cast=[ProviderType])
        )
