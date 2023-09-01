from kivymd.app import MDApp
from kivy.lang import Builder

class MyCardApp(MDApp):
    def build(self):
        return Builder.load_file('Example9.kv')
    
    def card_click(self):
        print("Card App Click!")  

if __name__ == '__main__':
    MyCardApp().run()
