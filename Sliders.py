
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image


Builder.load_file('Sliders.kv')
# Builder.load_string(''' copy builder file text here ''')
class  Sliders(Widget):
    def slide_it(self,*args):
        # print(args)
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1])*5)







class  slidersIt(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return  Sliders()

if __name__ == '__main__':
    slidersIt().run()

