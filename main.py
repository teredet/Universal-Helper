from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import weather, currency


Window.size = (480, 853)



class MainLayout(BoxLayout):
    def print_weather(self):
        json = weather.get_json(self.city.text)
        if json['cod'] == 200:
            self.weather_result.text = weather.get_info(json)
        else:
            self.weather_result.text = 'Invalid city'

    def print_currency(self):
        res = ''
        if currency.get_json('uah'):
            for i in currency.get_info(currency.get_json('uah'),  'uah', {'usd', 'eur'}):
                res += i + '\n'
        else:
            res = 'Invalid currency'

        self.curency_result.text = res
class HelperApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    HelperApp().run()
