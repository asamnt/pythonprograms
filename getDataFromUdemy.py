import requests
response = requests.get("https://www.udemy.com/api-2.0/users/me/subscribed-courses/?page=10")
print(response.text)