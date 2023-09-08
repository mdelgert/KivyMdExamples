#https://stackoverflow.com/questions/68854618/how-to-use-kivymd-bottom-navigation-to-switch-between-multiple-screens

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

for screen_name in [
    "master",
    "about",
    "contact",
    "home",
    "question"
    ]:
    
    Builder.load_file(f"{screen_name}.kv")

class Master(Screen):
    pass

class Home(Screen):
    def btn_question(self):
        print("btn_question")
        #self.root.ids.screen_manager.current = "question"
        #self.parent.parent.transition.direction = 'left'
        #self.parent.parent.current = 'question'
        
class About(Screen):
    pass

class Contact(Screen):
    pass

class Question(Screen):
    pass

class MainApp(MDApp):
    # def build(self):
    #     self.root = Master()
    #     self.theme_cls.material_style = "M2"
    #     self.theme_cls.theme_style = "Dark"
    #     return self.root

    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Master(name="master"))
        self.sm.add_widget(Home(name="home"))
        self.sm.add_widget(About(name="about"))
        self.sm.add_widget(Contact(name="contact"))
        self.sm.add_widget(Question(name="question"))
        #self.sm.current = 'question'
        return self.sm

    def change_screen(self, screen):
        print("change_screen")
        self.sm.current = screen

MainApp().run()