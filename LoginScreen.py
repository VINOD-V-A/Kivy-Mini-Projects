

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp



class LoginScreenMD(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('LoginScreen.kv')
    def logger(self):
        self.root.ids.welcome_label.text=f'{self.root.ids.user.text}'

    def clear(self):
        self.root.ids.welcome_label.text ="WelCome"
        self.root.ids.user.text = ""
        self.root.ids.psw.text = ""

LoginScreenMD().run()

