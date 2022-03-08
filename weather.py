import requests

from secretkey import API_KEY


def get_json(city, lang='en'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid':API_KEY,
        'q':city,
        'units':'metric',
        'lang':lang}

    return requests.get(url=url, params=params).json()

def get_info(weather):
    city = weather['name']
    country = weather['sys']['country']  # UA
    weather_now = weather['weather'][0]['description'].capitalize()
    temp = int(weather['main']['temp'])  # °C
    pressure = weather['main']['pressure']  # hPa
    humidity = weather['main']['humidity']  # %
    wind_speed = int(weather['wind']['speed'] * 3.6)  # from  meter/sec to km/hour

    return f'''
    {city},{country}
    {temp}°C - {weather_now}
    Humidity - {humidity}%
    Wind speed - {wind_speed} km/hour
    Atmospheric pressure - {pressure} hPa
    '''

if __name__ == '__main__':
    print(get_info(get_json('kiev')))