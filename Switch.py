
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.animation import Animation
# from kivy.uix.image import Image


Builder.load_file('Switch.kv')
# Builder.load_string(''' copy builder file text here ''')
class   SwitchIt(Widget):
    def switch_click(self,switchOnject,switchValue):
        if (switchValue):
            self.ids.my_label.text =" You click the switch on"
        else:
            self.ids.my_label.text = " You click the switch off"






class SwitchTap(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return SwitchIt()

if __name__ == '__main__':
    SwitchTap().run()

