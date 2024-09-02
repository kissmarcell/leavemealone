from flask import render_template

from src.entities.configuration import Configuration
from src.entities.workspace_with_issues import WorkspaceWithIssues
from src.enums.provider_type import ProviderType
from src.services.impl.asana_provider_service import AsanaProviderService
from src.services.impl.azure_devops_provider_service import AzureDevopsProviderService
from src.services.impl.jira_provider_service import JiraProviderService
from src.services.provider_service import ProviderService


class IndexController:
    @staticmethod
    def index():
        workspaces: list[WorkspaceWithIssues] = []
        for provider in Configuration.get().providers:
            service: ProviderService
            match provider.type:
                case ProviderType.JIRA:
                    service = JiraProviderService()
                case ProviderType.ASANA:
                    service = AsanaProviderService()
                case ProviderType.AZURE_DEVOPS:
                    service = AzureDevopsProviderService()
                case _:
                    raise Exception(f"Provider type {provider.type} is not supported")

            workspaces += service.get_issues_assigned_to_me(provider)
        return render_template('tasks.html', workspaces=workspaces)
