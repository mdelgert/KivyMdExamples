from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout

# KV language string for the main app layout
kv_string = '''
BoxLayout:
    orientation: 'vertical'

    ScrollView:
        BoxLayout:
            orientation: 'vertical'
            id: card_container
'''

class CardApp(MDApp):
    def build(self):
        self.root = Builder.load_string(kv_string)
        self.generate_cards()

    def generate_cards(self):
        card_container = self.root.ids.card_container
        for _ in range(3):  # Generate three cards
            card = MDCard(
                orientation="vertical",
                size_hint=(None, None),
                size=(200, 100),
                pos_hint={"center_x": 0.5},
                padding=15,
                md_bg_color=(1, 0.5, 0, 1),
                spacing=10,  # Spacing between card children
            )

            labels_layout = BoxLayout(orientation="vertical", spacing=20)  # Added spacing between labels

            label1 = MDLabel(
                text="Label 1",
                #theme_text_color="Primary",
                #font_style="H5",
            )
            label2 = MDLabel(
                text="Label 2",
                #theme_text_color="Primary",
                #font_style="H5",
            )

            # icon_button = MDIconButton(
            #     icon="android",
            #     pos_hint={"top": 1, "right": 1},
            # )
            # icon_button.bind(on_release=self.icon_click)

            labels_layout.add_widget(label1)
            labels_layout.add_widget(label2)

            card.add_widget(labels_layout)  # Add the labels layout to the card
            #card.add_widget(icon_button)
            card_container.add_widget(card)

    def icon_click(self, instance):
        # Handle the icon button click event here
        print("Icon Button Clicked")

if __name__ == '__main__':
    CardApp().run()
