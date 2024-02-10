
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('BackgroundTextColor.kv')
# Builder.load_string(''' copy builder file text here ''')
class Colour(Widget):
    pass



class colourAll(App):
    def build(self):
        return Colour()

if __name__ == '__main__':
    colourAll().run()

