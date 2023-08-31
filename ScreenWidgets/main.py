# https://kivymd.readthedocs.io/en/latest/themes/theming/

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

# Load the kv files for each screen
Builder.load_file("screen1.kv")
Builder.load_file("screen2.kv")
Builder.load_file("screen3.kv")

# Define the screen classes
class Screen1(Screen):
    def on_pre_enter(self):
        print("Screen1: on_pre_enter")   

    def on_enter(self):
        print("Screen1: on_enter")

class Screen2(Screen):
    def on_pre_enter(self):
        
        print("Screen2: on_pre_enter")
        
        #self.ids.screen2_label.text = 'Test!'

        for i in range(20):
            self.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )
            
    def on_enter(self):
        print("Screen2: on_enter")
        

class Screen3(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def on_start(self):
            print ("on_start")
            # for i in range(20):
            #     self.root.ids.container.add_widget(
            #         OneLineListItem(text=f"Single-line item {i}")
            #     )

MainApp().run()
