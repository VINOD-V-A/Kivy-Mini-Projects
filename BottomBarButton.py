from kivy.lang import Builder
from kivymd.app import MDApp



class BottomBarButton(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('BottomBarButton.kv')
    def presser(self):
        self.root.ids.my_label.text="You pressed it"

BottomBarButton().run()
