import requests
from secretkey import API_KEY

def get_info(city='Kyiv', lang='en'):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid':API_KEY,
              'q':city,
              'units':'metric',
              'lang':lang}

    return requests.get(url=url, params=params).json()



def main():
    print(get_info('Кривий Ріг', 'ua'))

if __name__ == '__main__':
    main()