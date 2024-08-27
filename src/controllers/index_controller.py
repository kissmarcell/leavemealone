from src.dto.configuration import Configuration
from src.services.impl.jira_provider_service import JiraProviderService
from src.services.provider_service import ProviderService


class IndexController:
    jira_provider_service: ProviderService = JiraProviderService()

    def index(self):
        for provider in Configuration.get().providers:
            print(provider)
        return self.jira_provider_service.get_issues_assigned_to_me(Configuration.get().providers[0])
