from enum import Enum


class ProviderType(str, Enum):
    JIRA = 'jira'
    ASANA = 'asana'
    AZURE_DEVOPS = 'azure_devops'
