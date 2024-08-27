from abc import ABC, abstractmethod


class ProviderService(ABC):
    @abstractmethod
    def get_issues_assigned_to_me(self, provider_config):
        pass
