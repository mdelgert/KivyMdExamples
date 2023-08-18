from kivy.lang import Builder
from kivymd.app import MDApp

class MenuApp(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("Menu1.kv")

# Run the app
if __name__ == "__main__":
    MenuApp().run()        