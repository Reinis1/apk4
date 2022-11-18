import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random
kivy.require("1.9.8")

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 100))

class Fakse(App):

    def build(self):
        return MyRoot()


fakse = Fakse()
fakse.run()
