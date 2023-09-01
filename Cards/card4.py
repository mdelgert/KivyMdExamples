from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton

KV = '''
MDFloatLayout:
    MDLabel:
        id: label0
        halign: 'center'
        markup: True
        text: "Cards"
        pos_hint: {'y': .45}

    MDCard:
        size_hint: None, None
        size: "300dp", "100dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}  # Center both horizontally and vertically

        BoxLayout:
            orientation: "vertical"

            Label:
                id: label1
                text: "Line 1"
                color: 1, 1, 1, 1
                font_size: "20sp"

            Label:
                id: label2
                text: "Line 2"
                color: 1, 1, 1, 1
                font_size: "20sp"
                size_hint_y: None
                height: self.texture_size[1]
                #halign: 'left'  # Left-align the text

            MDIconButton:
                icon: "android"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                on_release: app.icon_button_pressed()
'''
class MyApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def icon_button_pressed(self):
        print("Icon clicked!")

if __name__ == '__main__':
    MyApp().run()
