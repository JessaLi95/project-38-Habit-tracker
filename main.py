import requests
from datetime import datetime, timedelta
from decouple import config

# CREATE PROFILE
USERNAME = config('user_name')
TOKEN = config('token')
GRAPH_ID = "graph1"
profile_gen_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create = requests.post(profile_gen_endpoint, json=parameters)
print(create.text)

# POST
graph_endpoint = f"{profile_gen_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(graph.text)

# PUT
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.today()
yesterday = today - timedelta(days=1)
post_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "60"
}
post = requests.post(post_pixel_endpoint, json=post_config, headers=headers)
print(post.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/20220130"
update_config = {
    "quantity": "0"
}
update = requests.put(update_pixel_endpoint, json=update_config, headers=headers)
print(update.text)

# DELETE
delete_pixel_endpoint = f"{post_pixel_endpoint}/20220130"
delete = requests.delete(delete_pixel_endpoint, headers=headers)
print(delete.text)
