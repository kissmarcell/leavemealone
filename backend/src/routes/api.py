from abc import ABC

from flask import Blueprint

from src.controllers.index_controller import IndexController

class API(ABC):
    NAME_PATTERN: str = "api_{version}"
    ROUTE_PATTERN: str = "/api/{version}"
    blueprint: Blueprint

    @staticmethod
    def _blueprint(version: str):
        return Blueprint(
            API.NAME_PATTERN.format(version=version),
            __name__,
            url_prefix=f"{API.ROUTE_PATTERN.format(version=version)}"
        )

class APIv1(API):
    blueprint = API._blueprint("v1")

    @staticmethod
    @blueprint.route("/projects")
    def projects():
        return IndexController.get_data()
