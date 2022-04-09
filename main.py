from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

import weather, currency


Window.size = (480, 853)


class WeatherLayout(BoxLayout):
    def print_weather(self):           
        json = weather.get_json(self.city.text)
        if json['cod'] == 200:
            self.weather_result.text = weather.get_info(json)["weather"]
            self.img.source = weather.get_info(json)["img"]
        else:
            self.weather_result.text = 'Invalid city'


class CurrencyDropDown(DropDown):
    pass


class CurrencyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = CurrencyDropDown()   
    
    def print_currency(self):
        seccond_currencies = []
        toggleButtons = {
            self.dropdown.usd:'usd', 
            self.dropdown.eur:'eur', 
            self.dropdown.pln:'pln', 
            self.dropdown.rub:'rub',
            self.dropdown.gbp:'gbp',
            self.dropdown.jpy:'jpy',
            self.dropdown.turkish_lira:'try',
            self.dropdown.nok:'nok',
            self.dropdown.aed:'aed',
            self.dropdown.cny:'cny',
            self.dropdown.czk:'czk',
            self.dropdown.byn:'byn',}

        for toggleButton in toggleButtons.keys():
            if toggleButton.state == 'down':
                seccond_currencies.append(toggleButtons[toggleButton])
                
        if currency.get_json('uah'):
            res = currency.get_info(currency.get_json('uah'),  'uah', seccond_currencies)
            self.currency_result_main.text = res["main_res"]
            self.currency_result_reversed.text = res["reversed_res"]
        else:
            self.currency_result_main = 'Invalid currency'

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(WeatherLayout())
        self.add_widget(CurrencyLayout())
    
class HelperApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    HelperApp().run()
