import requests

# Base URL
base_url = 'https://jsonplaceholder.typicode.com/1'

response = requests.get(base_url)
if response.status_code == 200:
    print("Request successful.")
else:
    print("Request failed.")