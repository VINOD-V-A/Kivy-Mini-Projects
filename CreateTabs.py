
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
# from kivy.uix.image import Image


Builder.load_file('CreateTabs.kv')
# Builder.load_string(''' copy builder file text here ''')
class  CreateTabs(TabbedPanel):
    pass




class  MultiTabs(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return  CreateTabs()

if __name__ == '__main__':
    MultiTabs().run()

