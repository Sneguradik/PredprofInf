from cgitb import text
import kivy.app as app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

 
class MoneyCounterApp(app.App):
    def build(self):
        bl = BoxLayout()
        btn1 = Button(text = 'Hello')
        btn2 = Button(text = 'Something')
        bl.add_widget(btn1)
        bl.add_widget(btn2)
        return bl

if __name__ == "__main__":
    MoneyCounterApp().run()
