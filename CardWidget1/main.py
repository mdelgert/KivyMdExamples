from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('master.kv')
#Builder.load_file('customcard.kv')

class CustomCard(BoxLayout):
    pass

class Master(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        self.title = 'CardWidget1'
        self.root = Master()
        return self.root

if __name__ == '__main__':
    MyApp().run()