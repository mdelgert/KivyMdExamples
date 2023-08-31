# https://kivymd.readthedocs.io/en/latest/themes/theming/

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

# Load the kv files for each screen
Builder.load_file("screen1.kv")
Builder.load_file("screen2.kv")
Builder.load_file("screen3.kv")

# Define the screen classes
class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        # Not needed will load from main.kv and cause double firing of events
        #return Builder.load_file("main.kv")

MainApp().run()
