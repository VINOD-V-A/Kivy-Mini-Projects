
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
# from kivy.uix.image import Image


Builder.load_file('ProgressBars.kv')
# Builder.load_string(''' copy builder file text here ''')
class   ProgressBars(Widget):
    def press_it(self):
        current = self.ids.my_progress.value
        # if
        if current == 1:
            current =0
        #increment
        current += .25
        # update progress bar
        self.ids.my_progress.value = current

        # update label
        self.ids.my_label.text=f'{int(current*100)} % progress'






class Bars(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return ProgressBars()

if __name__ == '__main__':
    Bars().run()

