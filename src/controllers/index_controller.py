from src.entities.configuration import Configuration
from src.enums.provider_type import ProviderType
from src.services.impl.asana_provider_service import AsanaProviderService
from src.services.impl.jira_provider_service import JiraProviderService
from src.services.provider_service import ProviderService


class IndexController:
    @staticmethod
    def index():
        response = []
        for provider in Configuration.get().providers:
            service: ProviderService
            match provider.type:
                case ProviderType.JIRA:
                    service = JiraProviderService()
                case ProviderType.ASANA:
                    service = AsanaProviderService()
                case _:
                    raise Exception(f"Provider type {provider.type} is not supported")

            response += service.get_issues_assigned_to_me(provider)
        return response
