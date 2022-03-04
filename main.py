from pip import main
import requests


def get_info(city='Kyiv', lang='en'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid':'af655b4d6ea7e6619cf1f23c711647c8',
              'q':city,
              'units':'metric',
              'lang':lang}

    return requests.get(url=url, params=params).text



def main():
    print(get_info('Кривий Ріг', 'ua'))

if __name__ == '__main__':
    main()