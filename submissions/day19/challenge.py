import requests
import json

# SpaceX API Usage
base_url = 'https://api.spacexdata.com'
resource_path = '/v5/launches/latest'
endpoint_url = base_url + resource_path

response = requests.get(endpoint_url)

if response.status_code == 200:
    print("Latest SpaceX Launch Details")
    print("==============================")
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print("GET request failed.")