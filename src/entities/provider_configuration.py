from dataclasses import dataclass
from typing import Optional

from src.entities.workspace import Workspace
from src.enums.provider_type import ProviderType


@dataclass
class ProviderConfiguration:
    type: ProviderType
    email: Optional[str]
    token: str
    workspaces: list[Workspace]
