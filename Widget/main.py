from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

Builder.load_file('master.kv')
Builder.load_file('test.kv')

class TestWidget(Widget):
    label_text = StringProperty("Default Text")

class Master(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Master()

if __name__ == '__main__':
    MyApp().run()

