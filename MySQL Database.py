

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker
import mysql.connector



class DatabaseMD(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #DEfine Data base
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database="second_db",
        )

        # create a cursor
        c= mydb.cursor()
        #  Create DataBAse
        c.execute("CREATE DATABASE if not exists second_db")
        # # Check  to see if database was created
        # c.execute('SHOW DATABASES')
        # for db in c:
        #     print(db)


        # Create a tabel
        c.execute("""CREATE TABLE if not exists customer(name VARCHAR(55))""")
        # Check to see the table is created
        # c.execute("SELECT * FROM customer")
        # print(c.description)

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()
        return Builder.load_file('MySQL Database.kv')

    def submit(self):

        # Create Database or connect to one
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="second_db",
        )

        # create a cursor
        c = mydb.cursor()
        # Add the record
        sql_command = "INSERT INTO customer (name) VALUES(%s)"
        values = (self.root.ids.word_input.text,)

        # Execute SQL command
        c.execute(sql_command,values)



        # add little msg
        self.root.ids.word_label.text=f'{self.root.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.word_input.text =''

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()



    def show_records(self):
        # Create Database or connect to one
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="second_db",
        )

        # create a cursor
        c = mydb.cursor()

        # Grab record from database
        c.execute("Select * From customer")
        records= c.fetchall()

        word=''
        # loop
        for record in records:
            word=f'{word}\n{record[0]}'
            self.root.ids.word_label.text= f'{word}'

        # Commit our changes
        mydb.commit()

        # Close our connection
        mydb.close()






DatabaseMD().run()
