from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout

# KV language string for the main app layout
kv_string = '''
BoxLayout:
    orientation: 'vertical'

    GridLayout:
        cols: 1
        id: card_container

    MDRaisedButton:
        text: 'Add Card'
        on_release: app.add_card()
'''

class CardApp(MDApp):
    def build(self):
        self.root = Builder.load_string(kv_string)

    def add_card(self):
        card_container = self.root.ids.card_container
        if len(card_container.children) < 3:
            card = MDCard(
                orientation="vertical",
                size_hint=(None, None),
                size=(300, 200),
                pos_hint={"center_x": 0.5},
            )

            label = MDLabel(text="Card Label", halign="center")
            icon_button = MDIconButton(icon="android")

            card.add_widget(label)
            card.add_widget(icon_button)
            card_container.add_widget(card)

if __name__ == '__main__':
    CardApp().run()
