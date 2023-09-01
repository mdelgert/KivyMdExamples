from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    text = StringProperty()

class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file("card2.kv")  # Load the KV file

    def on_start(self):
        
        styles = {
            "elevated": "#f6eeee", 
            "filled": "#f4dedc", 
            "outlined": "#f8f5f4"
        }

        for style in styles.keys():
            self.root.ids.box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style=style,
                    text=style.capitalize(),
                    md_bg_color=styles[style],
                    shadow_offset=(0, -1),
                )
            )

Example().run()
