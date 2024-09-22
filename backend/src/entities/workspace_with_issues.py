from dataclasses import dataclass

from src.entities.issue import Issue
from src.enums.provider_type import ProviderType


@dataclass
class WorkspaceWithIssues:
    name: str
    issues: list[Issue]
    provider: ProviderType
