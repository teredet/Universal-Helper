import requests


def get_json(main_currency):
    url = f'http://www.floatrates.com/daily/{main_currency}.json'

    try:
        json = requests.get(url).json()
    except:
        json = 0
    return json

def get_info(rates, main_currency, seccond_currencies):
    main_res = 'Currency\n\n'
    reversed_res = 'Reversed currency\n\n'
    for currency in seccond_currencies:
        main_res += f"{rates[currency]['code']}/{main_currency.upper()} - {round(rates[currency]['inverseRate'], 2)}\n"
        reversed_res += f"{main_currency.upper()}/{rates[currency]['code']} - {round(rates[currency]['rate'], 2)}\n"
    
    
    return {'main_res':main_res, 'reversed_res':reversed_res}


if __name__ == '__main__':
    print(get_info(get_json('uah'), 'uah', {'usd', 'eur'}))
    # print(get_json('uah'))