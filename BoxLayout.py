import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('box.kv')
# Builder.load_string(''' copy builder file text here ''')
class MyLayout(Widget):
    pass



class box(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    box().run()

