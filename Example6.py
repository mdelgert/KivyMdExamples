from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("Example6.kv")  # Load the KV file

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

Example().run()