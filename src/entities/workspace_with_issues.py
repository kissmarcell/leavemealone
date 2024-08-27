from dataclasses import dataclass

from src.entities.issue import Issue


@dataclass
class WorkspaceWithIssues:
    name: str
    issues: list[Issue]