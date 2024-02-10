
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
# from kivy.uix.image import Image

#Define different screens
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass

class WindowManger(ScreenManager):
    pass


kv=Builder.load_file('MultipleWindows.kv')
# Builder.load_string(''' copy builder file text here ''')


class  Windows(App):
    def build(self):

        return kv

if __name__ == '__main__':
    Windows().run()

