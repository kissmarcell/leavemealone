import requests

from src.entities.issue import Issue
from src.entities.workspace_with_issues import WorkspaceWithIssues
from src.enums.asana_api_action_type import AsanaApiActionType
from src.services.provider_service import ProviderService


class AsanaProviderService(ProviderService):
    API_PATH = 'https://app.asana.com/api/1.0/'

    @staticmethod
    def get_issues_assigned_to_me(provider_config) -> list[WorkspaceWithIssues]:
        response = []
        for workspace in provider_config.workspaces:
            workspace_response = AsanaProviderService._make_request(
                AsanaApiActionType.TASKS,
                headers={"Authorization": f"Bearer {provider_config.token}"},
                params={'assignee': 'me', 'workspace': workspace.id})
            response.append(WorkspaceWithIssues(
                name=workspace.name,
                issues=AsanaProviderService._dict_to_issues(workspace_response),
                provider=provider_config.type
            ))
        return response

    @staticmethod
    def _make_request(action: AsanaApiActionType, headers: dict = None, params: dict = None):
        return requests.get(
            AsanaProviderService.API_PATH + action.value,
            headers=headers,
            params=params).json()

    @staticmethod
    def _dict_to_issues(data: dict) -> list[Issue]:
        return [Issue(
            id=task['gid'],
            name=task['name'],
            url=f"https://app.asana.com/0/{task['gid']}/{task['gid']}",
            state=''
        ) for task in data['data']]
