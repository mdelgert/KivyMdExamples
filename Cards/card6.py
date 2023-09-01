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
        pos_hint: {'y': .35}
        theme_text_color: "Custom"
        text_color: "orange"
        font_style: "H1"

    MDCard:
		orientation: "vertical"
		padding: "8dp"
		size_hint: None, None
		size: "200dp", "50dp"
		pos_hint: {"center_x": .5, "center_y": .5}
		MDLabel:
			text: "Line1"
            
		MDLabel:
			text: "Line2"           
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
