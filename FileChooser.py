
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image


Builder.load_file('FileChooser.kv')
# Builder.load_string(''' copy builder file text here ''')
class  FileChooser(Widget):
    def selected(self,filename):

        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])

        except:
            pass





class  chooser(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return  FileChooser()

if __name__ == '__main__':
    chooser().run()

