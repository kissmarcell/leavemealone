from src.dto.configuration import Configuration
from src.services.provider_service import ProviderService


class JiraProviderService(ProviderService):

    def get_issues_assigned_to_me(self):
        print(Configuration.get().providers)
        return 'current_app.config.keys()'
