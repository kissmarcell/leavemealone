import json

import requests

from src.entities.issue import Issue
from src.entities.provider_configuration import ProviderConfiguration
from src.entities.workspace import Workspace
from src.entities.workspace_with_issues import WorkspaceWithIssues
from src.enums.azure_devops_api_action_type import AzureDevopsApiActionType
from src.enums.request_type import RequestType
from src.services.provider_service import ProviderService


class AzureDevopsProviderService(ProviderService):
    API_PATH = 'https://dev.azure.com/{organization}/{project}/_apis/wit/{action}'
    WORK_ITEM_URL = "https://dev.azure.com/{organization}/{project}/_workitems/edit/{id}"
    WIQL_QUERY_PARAMS = {'api-version': '7.0'}
    WIQL_QUERY_DATA = {'query': 'SELECT [System.ID] FROM WorkItems WHERE [System.AssignedTo] = @Me'}
    WORK_ITEMS_FIELDS = ['System.State', 'System.Title']

    @staticmethod
    def get_issues_assigned_to_me(provider_config: ProviderConfiguration) -> list[WorkspaceWithIssues]:
        response = []
        for workspace in provider_config.workspaces:
            workspace_issues: list[Issue] = []
            ids_and_urls_response = AzureDevopsProviderService._make_request(
                AzureDevopsApiActionType.WIQL,
                RequestType.POST,
                workspace,
                provider_config,
                headers={'Content-Type': 'application/json'},
                params=AzureDevopsProviderService.WIQL_QUERY_PARAMS,
                data=AzureDevopsProviderService.WIQL_QUERY_DATA)
            for work_item in ids_and_urls_response['workItems']:
                workspace_issues.append(Issue(id=work_item["id"], url=AzureDevopsProviderService.WORK_ITEM_URL.format(
                    organization=provider_config.organization, project=workspace.id, id=work_item["id"]
                ), name='None', state=''))
            names_and_states_response = AzureDevopsProviderService._make_request(
                AzureDevopsApiActionType.WORKITEMS,
                RequestType.GET,
                workspace,
                provider_config,
                params={'ids': ','.join([str(issue.id) for issue in workspace_issues]), 'fields': ','.join(AzureDevopsProviderService.WORK_ITEMS_FIELDS)})
            for issue in workspace_issues:
                for work_item in names_and_states_response['value']:
                    if work_item['id'] == issue.id:
                        issue.name = work_item['fields']['System.Title']
                        issue.state = work_item['fields']['System.State']
            response.append(WorkspaceWithIssues(name=workspace.name, issues=workspace_issues))
        return response

    @staticmethod
    def _make_request(action: AzureDevopsApiActionType, request_type: RequestType, workspace: Workspace, provider_config: ProviderConfiguration, headers: dict = None, params: dict = None, data: dict = None):
        return requests.request(
            request_type.value,
            AzureDevopsProviderService.API_PATH.format(organization=provider_config.organization, project=workspace.id, action=action.value),
            auth=('', provider_config.token),
            headers=headers,
            params=params,
            data=json.dumps(data)).json()
