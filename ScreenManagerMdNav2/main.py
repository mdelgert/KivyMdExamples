from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

for screen_name in [
    "master",
    "about",
    "contact",
    "home",
    "question"
    ]:
    
    Builder.load_file(f"{screen_name}.kv")

class Master(MDScreen):
    pass

class Home(MDScreen):
    def btn_question(self):
        print("Home: btn_question")
        #self.root.ids.screen_manager.current = "question"
        self.parent.parent.transition.direction = 'left'
        self.parent.parent.current = 'question'
        
class About(MDScreen):
    pass

class Contact(MDScreen):
    pass

class Question(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        self.root = Master()
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        return self.root

MainApp().run()