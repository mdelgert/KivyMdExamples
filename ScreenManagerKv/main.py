from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# Load the kv files for each screen
Builder.load_file("screen1.kv")
Builder.load_file("screen2.kv")
Builder.load_file("screen3.kv")
Builder.load_file("splash.kv")
Builder.load_file("master.kv")

# Define the screen classes
class Screen1(Screen):
    def on_pre_enter(self):
        print("Screen1: on_pre_enter")
        try:
            self.ids.screen1_label.text = 'Test Screen1!'
        except Exception as error:
            print("Screen1 on_pre_enter exception occurred: ", error) # An exception occurred: division by zero

    def on_enter(self):
        print("Screen1: on_enter")

class Screen2(Screen):
    def on_pre_enter(self):
        print("Screen2: on_pre_enter")
    
    def on_enter(self):
        print("Screen2: on_enter")

class Screen3(Screen):
    def on_pre_enter(self):
        print("Screen3: on_pre_enter")
    
    def on_enter(self):
        print("Screen3: on_enter")

class Splash(Screen):
    def on_pre_enter(self):
        print("Splash: on_pre_enter")
    
    def on_enter(self):
        print("Splash: on_enter")

class MasterLayout(BoxLayout):
    def on_pre_enter(self):
        print("MasterLayout: on_pre_enter")
    
    def on_enter(self):
        print("MasterLayout: on_enter")

class MainApp(App):
    def build(self):
        #self.root = Builder.load_file("master.kv")
        self.root = MasterLayout()
        self.screen_manager = self.root.ids.screen_manager
        self.current_screen = "splash"
        #self.screen_manager.current = "screen1"
        #Clock.schedule_once(self.start_screen_rotation, 0.5)
        #Clock.schedule_interval(self.rotate_screens, 0.5)
        #Clock.schedule_interval(self.start_screen, 1)
        return self.root

    def start_screen(self, dt):
        print("start_screen")
        self.screen_manager.current = "screen1"

    def start_screen_rotation(self, dt):
        print("start_screen_rotation")
        Clock.schedule_interval(self.rotate_screens, 0.5)

    def rotate_screens(self, dt):
        print("rotate_screens")
        screen_names = ["splash", "screen1", "screen2", "screen3"]
        current_index = screen_names.index(self.current_screen)
        next_index = (current_index + 1) % len(screen_names)
        self.screen_manager.current = screen_names[next_index]
        self.current_screen = screen_names[next_index]

    def on_start(self):
        self.screen_manager.current = "screen1"
        print("on_start")

if __name__ == "__main__":
    MainApp().run()
