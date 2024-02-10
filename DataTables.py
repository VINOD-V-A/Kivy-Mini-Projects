from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp



class DataTablesMD(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
            pos_hint={"center_x":0.5, "center_y":0.5 },
            size_hint=(0.9, 0.6),
            check = True,
            use_pagination= True,
            rows_num =3,
            pagination_menu_height='240dp',
            pagination_menu_pos='auto',

            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                (" Email Address", dp(30)),
                ("Phone",dp(30))
            ],
            row_data =[
                ('Rana','raj','raj@gmail.com','123455'),
                ('TOM','TOMAn','tom@gmail.com','156474'),
                ('Jerry','jer','jerry@gmail.com','476474'),
                ('Rana', 'raj', 'raj@gmail.com', '123455'),
                ('TOM', 'TOMAn', 'tom@gmail.com', '156474'),
                ('Jerry', 'jer', 'jerry@gmail.com', '476474'),
                ('Rana', 'raj', 'raj@gmail.com', '123455'),
                ('TOM', 'TOMAn', 'tom@gmail.com', '156474'),
                ('Jerry', 'jer', 'jerry@gmail.com', '476474')

            ]
        )
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('DataTables.kv')
        screen.add_widget(table)
        return screen

    #Function for check press
    def checked(self, instance_table,current_row):
        print(instance_table,current_row)

    # Function for row press
    def row_checked(self, instance_table, instance_row):
        print(instance_table,instance_row)





    # click ok
    def on_save(self, instance, value, date_range):
        self.root.ids.date_label.text = str(value)




DataTablesMD().run()
