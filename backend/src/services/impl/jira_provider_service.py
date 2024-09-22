from typing import List

import requests

from src.entities.issue import Issue
from src.entities.provider_configuration import ProviderConfiguration
from src.entities.workspace import Workspace
from src.entities.workspace_with_issues import WorkspaceWithIssues
from src.enums.jira_api_action_type import JiraApiActionType
from src.services.provider_service import ProviderService


class JiraProviderService(ProviderService):
    API_PATH = 'https://{}.atlassian.net/rest/api/3/'
    WORK_ITEM_URL = "https://{workspace}.atlassian.net/browse/{id}"
    QUERY_HEADERS = {'Accept': 'application/json'}
    QUERY_PARAMS = {'jql': 'assignee=currentUser()'}
    TASK_NAME_FORMAT = '[{key}]{summary}'

    @staticmethod
    def get_issues_assigned_to_me(provider_config) -> list[WorkspaceWithIssues]:
        response = []
        for workspace in provider_config.workspaces:
            workspace_response = JiraProviderService._make_request(
                provider_config,
                workspace,
                JiraApiActionType.SEARCH,
                headers=JiraProviderService.QUERY_HEADERS,
                params=JiraProviderService.QUERY_PARAMS)
            response.append(WorkspaceWithIssues(
                name=workspace.name,
                issues=JiraProviderService._dict_to_issues(workspace_response, workspace),
                provider=provider_config.type
            ))
        return response

    @staticmethod
    def _make_request(provider_config: ProviderConfiguration, workspace: Workspace, action: JiraApiActionType,
                      headers: dict = None, params: dict = None):
        return requests.get(
            JiraProviderService.API_PATH.format(workspace.id) + action.value,
            auth=(provider_config.email, provider_config.token),
            headers=headers,
            params=params).json()

    @staticmethod
    def _dict_to_issues(data: dict, workspace: Workspace) -> List[Issue]:
        return [Issue(
            id=task['key'],
            name=JiraProviderService.TASK_NAME_FORMAT.format(key=task['key'], summary=task['fields']['summary']),
            url=JiraProviderService.WORK_ITEM_URL.format(workspace=workspace.id, id=task['key']),
            state=task['fields']['status']['name']
        ) for task in data['issues']]
