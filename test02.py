import requests



#response = requests.get(complete_url)
#print(response.json)

def get_weather_API(city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '4c47146bdd9e9fc59ae3f1d7a5bd0008'
    complete_url = f'{base_url}&appid={api_key}&q={city}'
    response = requests.get(complete_url)
    return response.json()

def get_weather_temp(city):
    response = get_weather_API(city)
    temp = response['main']['temp']
    return round((temp - 273.15), 2)

def get_weather_main(city):
    response = get_weather_API(city)
    main = response['weather'][0]['main']
    return main

print(get_weather_temp('Rio de Janeiro'))
print(get_weather_main('Rio de Janeiro'))