#on_enter not working on starting screen of app
#https://stackoverflow.com/questions/32553320/on-enter-firing-before-screen-is-entered-when-using-nested-screenmanager-in-kivy
#https://www.reddit.com/r/kivy/comments/160guv3/on_enter_not_working_on_starting_screen_of_app/

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition
from kivy.clock import Clock

kv = """
<EventScreen@Screen>:
    on_enter: print(f'Entering {self.name} screen')
    on_leave: print(f'Leaving {self.name} screen')
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: root.name
        Button:
            size_hint_y: None
            height: dp(38)
            text: 'Next'
            on_release: root.manager.current = root.manager.next()
            
ScreenManager:
    EventScreen:
        name: 'dummy'
    EventScreen:
        name: 'first'
    EventScreen:
        name: 'second'
"""


class ScreenOrderApp(App):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        saved_transition = self.root.transition
        self.root.transition = NoTransition()
        self.root.current = 'first'
        self.root.transition = saved_transition
        Clock.schedule_once(self.remove_dummy)

    def remove_dummy(self, _):
        self.root.remove_widget(self.root.get_screen('dummy'))


ScreenOrderApp().run()