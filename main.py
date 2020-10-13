from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        layout = FloatLayout()
        ti = TextInput(text='Hello world', multiline=False)
        layout.add_widget(ti)
        return layout

if __name__ == "__main__":
    MainApp().run()