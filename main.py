import requests
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

from secretkey import API_KEY


class HelperApp(App):
    
    def get_json(self, city='Kyiv', lang='en'):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'appid':API_KEY,
            'q':city,
            'units':'metric',
            'lang':lang}

        return requests.get(url=url, params=params).json()

    def get_info(self, weather):
        city = weather['name']
        country = weather['sys']['country']  # UA
        weather_now = weather['weather'][0]['description'].capitalize()
        temp = int(weather['main']['temp'])  # °C
        pressure = weather['main']['pressure']  # hPa
        humidity = weather['main']['humidity']  # %
        wind_speed = int(weather['wind']['speed'] * 3.6)  # from  meter/sec to km/hour

        self.result.text = f'''
        {city},{country}
        {temp}°C - {weather_now}
        Humidity - {humidity}%
        Wind speed - {wind_speed} km/hour
        Atmospheric pressure - {pressure} hPa
        '''

    def print_weather(self, instance):
        json = self.get_json(self.city.text)
        self.get_info(json)

    def build(self):
        Window.size = (300, 600)

        root = BoxLayout(orientation='vertical')

        topBox = BoxLayout(orientation='vertical', size_hint=[1,0.2])
        topBox.add_widget(Label(text='Enter your city:', size_hint=[1,.2]))
        root.add_widget(topBox)

        midleBox = BoxLayout(orientation='vertical', size_hint=[1,.1])
        self.city = TextInput(
            text = '', readonly = False, font_size = 25, 
            background_color = [1,1,1,.5],
            foreground_color = (1,1,1,1), cursor_color = (1,1,1,1)
        )
        midleBox.add_widget(self.city)
        midleBox.add_widget(Button(text='Enter', on_press = self.print_weather))
        self.result = TextInput(readonly=True)

        root.add_widget(midleBox)

        bottomBox = BoxLayout(orientation='horizontal', size_hint=[1,.4])
        bottomBox.add_widget(self.result)

        root.add_widget(bottomBox)

        return root

if __name__ == '__main__':
    HelperApp().run()
