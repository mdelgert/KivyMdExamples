from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# Load the kv files for each screen
Builder.load_file("master.kv")
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
    
    def on_enter(self):
        print("Screen2: on_enter")

class Screen3(Screen):
    def on_pre_enter(self):
        print("Screen2: on_pre_enter")
    
    def on_enter(self):
        print("Screen2: on_enter")

class MasterLayout(BoxLayout):
    def on_pre_enter(self):
        print("MasterLayout: on_pre_enter")
    
    def on_enter(self):
        print("MasterLayout: on_enter")

class MainApp(App):
    def build(self):
        self.title = 'Demo'
        layout = MasterLayout()
        return layout
    
    def on_start(self):
        print("on_start")

if __name__ == "__main__":
    MainApp().run()
