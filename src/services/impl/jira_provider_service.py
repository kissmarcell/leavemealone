import requests

from src.dto.configuration import ProviderConfiguration
from src.services.provider_service import ProviderService


class JiraProviderService(ProviderService):

    def get_issues_assigned_to_me(self, provider_config: ProviderConfiguration):
        data = self.make_request(provider_config, '/rest/api/3/search', {'jql': 'assignee=currentUser()'})
        return data

    def make_request(self, provider_config: ProviderConfiguration, path: str, params: dict):
        return requests.get(
            provider_config["url"] + path,
            auth=(provider_config["email"], provider_config["token"]),
            headers={'Accept': 'application/json'}, params=params).json()
