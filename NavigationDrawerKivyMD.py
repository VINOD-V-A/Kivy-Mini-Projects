from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout
from kivymd.uix.list import MDList,OneLineIconListItem,IconLeftWidget
Window.size = (300,500)

Navigation_helper ="""
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title:"Demo application"
                        left_action_items: [["menu",lambda x: nav_drawer.set_state('open')]]
                        elevation: 5
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding: '8dp'
                
                Image:
                    source:'login.jpg'
                
                MDLabel:
                    text:"  Welcome"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text:"  Email"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Profile"
                            IconLeftWidget:
                                icon:"android"
                            
                            
                            
                       
                                       
"""

class NavigationDrawerKivyMD(MDApp):
    def build(self):
        screen = Builder.load_string(Navigation_helper)
        return screen




NavigationDrawerKivyMD().run()


