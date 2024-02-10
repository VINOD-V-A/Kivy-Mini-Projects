
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image


Builder.load_file('CheckboxAndRadioButton.kv')
# Builder.load_string(''' copy builder file text here ''')
class  CreateCheckBoxes(Widget):
    check = []
    def checkbox_click(self,instance, value,topping):

        if value == True:
            CreateCheckBoxes.check.append(topping)
            tops =""
            for x in CreateCheckBoxes.check:
                tops=f'{tops} {x}'
            self.ids.output_label.text = f"You Selected:{tops} "
        else:
            CreateCheckBoxes.check.remove(topping)
            tops = ""
            for x in CreateCheckBoxes.check:
                tops = f'{tops} {x}'
            self.ids.output_label.text = f"You Selected:{tops} "


class  check(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return  CreateCheckBoxes()

if __name__ == '__main__':
    check().run()

