import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://granitalapkezelo.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth()

headers = {
    "Accept": "application/json"
}

query = {
    'jql': 'assignee = currentUser()',
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
