import requests


def get_json(main_currency):
    url = f'http://www.floatrates.com/daily/{main_currency}.json'

    try:
        json = requests.get(url).json()
    except:
        json = 0
    return json

def get_info(rates, main_currency, seccond_currencies):
    res = set()
    for currency in seccond_currencies:
        res.add(f"{rates[currency]['code']}/{main_currency.upper()} - {round(rates[currency]['inverseRate'], 2)}")

    return res


if __name__ == '__main__':
    # print(get_info(get_json('uah'), 'uah', {'usd', 'eur'}))
    print(get_json('ua'))