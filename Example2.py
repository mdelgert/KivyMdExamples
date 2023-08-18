from kivy.lang import Builder
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.chip import MDChip

root_kv = """
BoxLayout:
    MDRaisedButton:
        text: app.title
        on_release: app.title = "Abcd"

    MyWidget:
"""


class MyWidget(MDChip):
    def __init__(self, **kwargs):
        self.label = App.get_running_app().title
        super().__init__(**kwargs)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()