import requests

#

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = '4c47146bdd9e9fc59ae3f1d7a5bd0008'
city = "Rio"
complete_url = f'{base_url}&appid={api_key}&q={city} '