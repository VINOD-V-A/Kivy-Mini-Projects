from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class VideoPly(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # Create videoplayer Instance
        player = VideoPlayer(source="Bean.mp4")

        #Assign Videoplayer
        player.state= 'play'
        # Set options
        player.options = {'eos': 'loop'}
        # Allow Stretch
        player.allow_stretch = True
        # Return player
        return player



VideoPly().run()
