from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<MD3Card>
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:

        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}
            on_release: 
                root.card_click()
                app.card_click()

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True

MDScreen:

    MDBoxLayout:
        id: box
        orientation: 'vertical'
        adaptive_size: True
        spacing: "56dp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    text = StringProperty()
    def card_click(self):
        print("Card App Click!")   

class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def card_click(self):
        print("Card Root Click!")  

    def on_start(self):
        
        # styles = {
        #     "elevated": "#f6eeee", 
        #     "filled": "#f4dedc", 
        #     "outlined": "#f8f5f4"
        # }

        styles = {
            "elevated": "#FFA500", 
            "filled": "#FFA500", 
            "outlined": "#FFA500"
        }

        count = 0

        for style in styles.keys():
            count += 1

            self.root.ids.box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="outlined",
                    #text=style.capitalize(),
                    text="TEST" + str(count),
                    md_bg_color=styles[style],
                    shadow_offset=(0, -1),
                )
            )


Example().run()