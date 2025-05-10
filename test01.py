import requests

response = requests.get('https://api.github.com/users/devAnnaEliza')

# check if the request was successful
print(response.status_code)