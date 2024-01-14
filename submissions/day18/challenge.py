import requests

base_url = 'http://127.0.0.1:5000/views/about'
resource_path = '/posts'
endpoint_url = base_url + resource_path

headers = {
    "User-Agent": "MyApp/1.0"
}

get_response = requests.get(endpoint_url, headers=headers)
print("GET RESPONSE DETAILS")
print(f"HTTP status code: {get_response.status_code}\nHeaders: {get_response.headers}\nContent: {get_response.text}\n\n")

data = {
    'title': 'API Testing',
    'body': 'This is an API testing which tests the typicode API.'
}

post_response = requests.post(endpoint_url, json=data)
print("POST RESPONSE DETAILS")
print(f"HTTP status code: {post_response.status_code}\nContent: {post_response.text}")

