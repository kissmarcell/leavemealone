from typing import List

import requests

from src.entities.issue import Issue
from src.entities.provider_configuration import ProviderConfiguration
from src.entities.workspace import Workspace
from src.entities.workspace_with_issues import WorkspaceWithIssues
from src.enums.jira_api_action_type import JiraApiActionType
from src.services.provider_service import ProviderService


class JiraProviderService(ProviderService):
    JIRA_API_PATH = 'https://{}.atlassian.net/rest/api/3/'
    QUERY_HEADERS = {'Accept': 'application/json'}
    QUERY_PARAMS = {'jql': 'assignee=currentUser()'}

    @staticmethod
    def get_issues_assigned_to_me(provider_config) -> List[WorkspaceWithIssues]:
        response = []
        for workspace in provider_config.workspaces:
            workspace_response =  JiraProviderService._make_request(
                provider_config,
                workspace,
                JiraApiActionType.SEARCH,
                headers=JiraProviderService.QUERY_HEADERS,
                params=JiraProviderService.QUERY_PARAMS)
            response.append(WorkspaceWithIssues(
                name=workspace.name,
                issues=JiraProviderService._dict_to_issues(workspace_response)
            ))
        return response

    @staticmethod
    def _make_request(provider_config: ProviderConfiguration, workspace: Workspace, action: JiraApiActionType, headers: dict = None, params: dict = None):
        return requests.get(
            JiraProviderService.JIRA_API_PATH.format(workspace.id) + action.value,
            auth=(provider_config.email, provider_config.token),
            headers=headers,
            params=params).json()

    @staticmethod
    def _dict_to_issues(data: dict) -> List[Issue]:
        return [Issue(
            id=task['id'],
            name=task['key'],
            url=task['self']
        ) for task in data['issues']]