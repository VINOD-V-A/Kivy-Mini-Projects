from kivy_garden.mapview import MapView
from kivymd.app import MDApp





class AddMap(MDApp):
    def build(self):
        mapview = MapView()
        return mapview



AddMap().run()
