import requests

api_url = 'https://settings.svc.halowaypoint.com/settings/hipc/e2a0a7c6-6efe-42af-9283-c2ab73250c48'

response = requests.get(url=api_url)
print(response.text)