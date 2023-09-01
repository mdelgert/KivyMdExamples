from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('slider3.kv')

class MyApp(App):
    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    pass

if __name__ == '__main__':
    MyApp().run()





