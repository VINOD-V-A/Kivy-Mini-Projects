from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker



class TimePickerMD(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('TimePicker.kv')

    def get_time(self,instance,time):
        self.root.ids.time_label.text= str(time)

    def on_cancel(self,instance,time):
        self.root.ids.time_label.text = "You Clicked"



    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel = self.on_cancel, time= self.get_time)
        time_dialog.open()


    # click ok
    def on_save(self, instance, value, date_range):
        self.root.ids.date_label.text = str(value)




TimePickerMD().run()
