import requests


api_key = "insert_key_here"
base = "http://api.openweathermap.org/data/2.5/weather?"




city = input("Enter a city: ")
url = base + "appid=" + api_key+ "&q="+city


def kelvin_to_celcius(kelvin):
    c = kelvin - 273.15
    return c



response = requests.get(url).json()
#print(response)

if response['cod'] == 200:
    ci_ty = response['name']
    country = response['sys']['country']
    weatherinfo = response['weather'][0]
    weather = weatherinfo['main']
    weather_desc = weatherinfo['description']
    temp_k = response['main']['temp']
    feelslike = response['main']['feels_like']
    humidity = response['main']['humidity']


    print(f"Weather in {ci_ty},{country}: \n{weather}, {weather_desc}")
    print(f"Temp: {kelvin_to_celcius(temp_k)}")
    print(f"Feels like: {kelvin_to_celcius(feelslike)}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error: {response['cod']}")


her\ app.py 



