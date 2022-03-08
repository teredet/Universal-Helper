from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import weather


Window.size = (480, 853)



class MainLayout(BoxLayout):
    def print_weather(self):
        json = weather.get_json(self.city.text)
        if json['cod'] == 200:
            self.result.text = weather.get_info(json)
        else:
            self.result.text = 'Invalid city'

class HelperApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    HelperApp().run()
