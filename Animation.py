
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
# from kivy.uix.image import Image


Builder.load_file('Animation.kv')
# Builder.load_string(''' copy builder file text here ''')
class   AnimationNow(Widget):
    def animate_it(self,widget,*args):
        #Define the animation
        animate= Animation(
            background_color=(0,0,1,1),
            duration=1)
        # second animation
        animate += Animation(size_hint=(1, 1))
        # third animation
        animate += Animation(size_hint=(.5, .5))
        # forth animation
        animate += Animation(pos_hint={"center_x":0.2})
        animate += Animation(pos_hint={"center_x": 0.5})


        # start the animation
        animate.start(widget)

        # create call back
        animate.bind(on_complete=self.my_callback)

    def my_callback(self,*args):
        self.ids.my_label.text="Bye"





class AniApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return AnimationNow()

if __name__ == '__main__':
    AniApp().run()

