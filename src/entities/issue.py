from dataclasses import dataclass


@dataclass
class Issue:
    id: str
    name: str
    url: str