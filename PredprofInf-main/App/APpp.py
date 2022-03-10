import kivy.app as app
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (414, 736)

'''class Main(Screen):
    Username = 'Max'
    Currency = '$'
    CurrentCurrency = 'Цены указаны в '+ Currency
    Perriod = 'March'
    Balance = '50000'
    op1 = 'Бутылка молока'
    c1 = '-50 р'
    '''
    

class Balance(Screen):
    pass

class Op_Menu(Screen):
    #cur = 'р'
    #с1 = '-50' + cur
    #op = 'Бутылка молока' + с1
    pass

class Extra(Screen):
    pass

class AllOp(Screen):
    pass

class Costs(Screen):
    pass

class Operation_Change(Screen):
    pass

class Add_New_Op(Screen):
    pass

class Op_Menu(Screen):
    pass

class MoneyCounterApp(app.App):
    
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(Balance(name='Balance'))
        #sm.add_widget(Op_Menu(name='Op_Menu'))
        #sm.add_widget(Operation_Change(name='Operation_Change'))
        sm.add_widget(Add_New_Op(name='Add_New_Op'))
        sm.add_widget(AllOp(name='AllOp'))
        sm.add_widget(Extra(name='Extra'))
        sm.add_widget(Costs(name='Costs'))
        return sm



if __name__ == "__main__":
    MoneyCounterApp().run()