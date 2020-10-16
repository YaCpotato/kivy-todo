from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class List(BoxLayout):
    def __init__(self, **kwargs):
        super(List, self).__init__(**kwargs)
        self.rv.data = []
        btn_list = ['ひつまぶし','味噌煮込みうどん','味噌カツ','台湾ラーメン' \
                    ,'手羽先','小倉トースト','きしめん','あんかけスパ','どて煮' \
                    ,'ういろう','甘口バナナスパ']
        for btn_list_any in btn_list:
            self.rv.data.append({'value': btn_list_any})


class MainApp(App):
    def build(self):
        layout = FloatLayout()
        todo_list = List()
        ti = TextInput(text='Hello world', multiline=False)
        layout.add_widget(ti)
        layout.add_widget(todo_list)

        return layout

if __name__ == "__main__":
    MainApp().run()