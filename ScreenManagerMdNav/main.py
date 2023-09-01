# https://kivymd.readthedocs.io/en/latest/themes/theming/
# https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.app import MDApp
from kivy.uix.popup import Popup

# Load the kv files for each screen
for screen_name in [
    "master",
    "home",
    "about",
    "contact",
    "popup"
    ]:
    
    Builder.load_file(f"screens/{screen_name}.kv")

# Define the screen classes
class Home(Screen):
    def show_popup(self):
        print("show_popup pressed")
        popup = MyPopup()
        popup.open()

class MyPopup(Popup):
    def dismiss_popup(self):
        self.dismiss()  # Dismiss the popup
    
    def btn_hello(self):
        print("btn_home pressed")
        self.ids.pop_label.text = "Hello Pop!"

class About(Screen):
    pass

class Contact(Screen):
    pass

class Master(BoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        self.root = Master()
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.root.ids.screen_manager.transition = NoTransition()
        return self.root

MainApp().run()
