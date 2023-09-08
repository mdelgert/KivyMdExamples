from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

# Create HomeScreen class (unchanged)
class HomeScreen(MDScreen):
    def open_question_screen(self):
        self.parent.parent.transition.direction = 'left'
        self.parent.parent.current = 'screen_question'

# Create QuestionScreen class (unchanged)
class QuestionScreen(MDScreen):
    pass

# Create AboutScreen class (unchanged)
class AboutScreen(MDScreen):
    pass

# Create MainApp class
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        #return Builder.load_file("main.kv")

if __name__ == "__main__":
    MainApp().run()
