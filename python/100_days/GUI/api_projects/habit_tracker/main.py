import requests
from datetime import datetime

USERNAME = "devsamurai"
TOKEN = "pixelakey"
MY_GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Writing Graph",
#     "unit": "page",
#     "type": "int",
#     "color": "momiji"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}"
headers = {
    "X-USER-TOKEN": TOKEN
}
# today = datetime(year=2023, month=6, day=13)
# graph_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "5"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime(year=2023, month=6, day=13)
now = today.strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}/{now}"
# print(update_endpoint)
update_params = {
    "quantity": "15",
}
response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)
