import mysql.connector
import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window

Window.size = (320, 680)
myDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='balayan_taxpayer'
)

myCursor = myDb.cursor()


class WindowManager(ScreenManager):
    pass


class SecondPage(Screen):
    pass


class HomePage(Screen):
    Config.set("graphics", "width", "320")
    Config.set("graphics", "height", "680")
    Config.set("graphics", "borderless", "0")
    Config.set("graphics", "resizable", "0")

    def access_page2(self):
        if myDb.is_connected():
            self.manager.current = "page2"


# Designate Our .kv file
kv = Builder.load_file('sample.kv')


class SampleApp(MDApp):
    def build(self):
        return kv


if __name__ == "__main__":
    SampleApp().run()