#from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def on_pre_enter(self):
        print("Main pre enter")
        self.ids.main_label.text = 'Home screen text updated.'       

class SettingsScreen(Screen):
    def on_pre_enter(self):
        print("Settings pre enter")
        self.ids.settings_label.text = 'Settings screen text updated.'         

class MyApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        return self.sm

    def settings_screen_opened(self):
        print("Settings screen opened")

if __name__ == '__main__':
    Builder.load_file('main.kv')
    Builder.load_file('settings.kv')
    MyApp().run()
