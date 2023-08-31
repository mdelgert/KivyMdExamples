#from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem

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

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        return sm

if __name__ == '__main__':
    Builder.load_file('screen1.kv')
    Builder.load_file('screen2.kv')
    MyApp().run()
