#from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import NoTransition
from kivy.clock import Clock

Builder.load_file('master.kv')
Builder.load_file('splash.kv')
Builder.load_file('screen1.kv')
Builder.load_file('screen2.kv')

class Screen1(Screen):
    def on_pre_enter(self):
        print("Screen1: on_pre_enter")
        try:
            #self.ids.screen1_label.text = 'Test Screen1!'
            for i in range(20):
                self.ids.scroll1.add_widget(
                    OneLineListItem(text=f"Single-line item {i}")
                )

        except:
            print('Screen2: on_pre_enter: error')   

    def on_enter(self):
        print("Screen1: on_enter")

class Screen2(Screen):

    def on_pre_enter(self):
        print("Screen2: on_pre_enter")
        try:
            self.ids.screen2_label.text = 'Test Screen2!'
            # for i in range(20):
            #     self.ids.scroll2.add_widget(
            #         OneLineListItem(text=f"Single-line item {i}")
            #     )   
        except:
            print('Screen2: on_pre_enter: error') 

    def on_enter(self):
        print("Screen2: on_enter")

class Splash(Screen):
    def on_pre_enter(self):
        print("Splash: on_pre_enter")

    def on_enter(self):
        print("Splash: on_enter")
        #self.ids.screen_manager.current = 'screen1'
        #self.root.screen_manager = 'screen1'

class Master(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        self.title = 'Screen Manager'
        self.root = Master()
        self.screen_manager = self.root.ids.screen_manager
        self.current_screen = "splash"
        return self.root

    def on_start(self):
        print("on_start")
        self.screen_manager.current = "screen1"

    def remove_splash(self, _):
        print("remove_splash")

if __name__ == '__main__':
    MyApp().run()
