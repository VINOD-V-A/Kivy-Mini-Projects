import sqlite3

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
import sqlite3



class DatabaseMD(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #Create Database or connect to one
        conn = sqlite3.connect('first_db.db')

        # create a cursor
        c= conn.cursor()
        # Create a tabel
        c.execute("""CREATE TABLE if not exists customer(name text)""")

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()
        return Builder.load_file('DatabaseMD.kv')

    def submit(self):

        # Create Database or connect to one
        conn = sqlite3.connect('first_db.db')

        # create a cursor
        c = conn.cursor()
        # Add the record
        c.execute("INSERT INTO customer VALUES(:first)",{'first':self.root.ids.word_input.text})

        # add little msg
        self.root.ids.word_label.text=f'{self.root.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.word_input.text =''

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()



    def show_records(self):
        # Create Database or connect to one
        conn = sqlite3.connect('first_db.db')

        # create a cursor
        c = conn.cursor()

        # Grab record from database
        c.execute("Select * From customer")
        records= c.fetchall()

        word=''
        # loop
        for record in records:
            word=f'{word}\n{record[0]}'
            self.root.ids.word_label.text= f'{word}'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()






DatabaseMD().run()
