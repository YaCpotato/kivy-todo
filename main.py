from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder       

class MainApp(App):
    def build(self):
        Builder.load_file('./main.kv')
        layout = FloatLayout()
        self.rv.data = []
        btn_list = ['ひつまぶし','味噌煮込みうどん','味噌カツ','台湾ラーメン' \
                    ,'手羽先','小倉トースト','きしめん','あんかけスパ','どて煮' \
                    ,'ういろう','甘口バナナスパ']
        for btn_list_any in btn_list:
            self.rv.data.append({'value': btn_list_any})
        ti = TextInput(text='Hello world', multiline=False)
        layout.add_widget(ti)
        layout.add_widget(todo_list)

        return layout

if __name__ == "__main__":
    MainApp().run()