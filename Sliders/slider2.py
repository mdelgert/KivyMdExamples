# without kivymd this works!

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SliderExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        self.label = Label(text="Slider Value: 50", size_hint=(1, 0.2))
        self.slider = Slider(min=0, max=100, value=50, size_hint=(1, 0.6))
        self.slider.bind(value=self.on_slider_value_change)
        
        layout.add_widget(self.label)
        layout.add_widget(self.slider)
        
        return layout
    
    def on_slider_value_change(self, instance, value):
        self.label.text = f"Slider Value: {int(value)}"

if __name__ == '__main__':
    SliderExample().run()
