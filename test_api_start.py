import requests

url = "https://api.chucknorris.io/jokes/random"
result = requests.get(url)
check = result.json()
check_info = check.get("created_at")
print(url)
print(check)
print(check_info)
