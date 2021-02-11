from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(200, 200))
        s.add_widget(fl)
        fl.add_widget(Button(
            text="Это кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1,1,0,1],
            background_normal='',
            size_hint=(.75, .5),
            pos=(50, 100)));
        return s
    def btn_press(self, instance):        
        instance.text='Я нажата'
        instance.font_size=36
        
if __name__=="__main__":
    myApp().run()
