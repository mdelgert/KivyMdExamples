from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.button import MDRaisedButton

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

        # Check a condition to hide the "Question" screen
        if not self.should_show_question_screen():
            self.root.ids.bottom_navigation.remove_widget(self.root.ids.screen_question)
        
        return Builder.load_file("main.kv")

    def should_show_question_screen(self):
        # Add your condition to determine whether to show the "Question" screen
        # For example, you can return True to always show it, or False to hide it
        return True

if __name__ == "__main__":
    MainApp().run()
