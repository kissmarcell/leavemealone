from abc import ABC, abstractmethod

from src.entities.provider_configuration import ProviderConfiguration
from src.entities.workspace_with_issues import WorkspaceWithIssues


class ProviderService(ABC):
    @staticmethod
    @abstractmethod
    def get_issues_assigned_to_me(provider_config: ProviderConfiguration) -> list[WorkspaceWithIssues]:
        pass
