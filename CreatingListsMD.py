from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from   kivymd.uix.list import MDList,ThreeLineListItem,ThreeLineIconListItem,IconLeftWidget,ThreeLineAvatarIconListItem
from   kivymd.uix.list import ImageLeftWidget
from kivymd.uix.scrollview import ScrollView

class CreatingLists(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)
        for i in range(20):
            # icon= IconLeftWidget(icon="android")
            img= ImageLeftWidget(source='log2.jpg')
            items = ThreeLineIconListItem(text='Items '+ str(i),secondary_text="Hello World",tertiary_text='Third Text')
            items.add_widget(img)
            list_view.add_widget(items)


        screen.add_widget(scroll)

        return screen

CreatingLists().run()