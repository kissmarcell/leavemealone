from src.services.impl.jira_provider_service import JiraProviderService
from src.services.provider_service import ProviderService


class IndexController:
    jira_provider_service: ProviderService = JiraProviderService()

    def index(self):
        return self.jira_provider_service.get_issues_assigned_to_me()
