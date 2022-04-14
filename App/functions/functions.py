import sqlite3
import csv
import datetime


def new_cost(user_id, category_id, amount, date, currency, Title=None, Content=None):  # добавить новый расход
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''insert into Costs(user_id, category_id, amount, date, currency, Title, Content) values
({user_id}, {category_id}, {amount}, {date.strftime('%Y-%m-%d')}, "{currency}", {'"' + Title + '"' if Title else "NULL"}, 
{'"' + Content + '"' if Content else "NULL"})'''
        cursor.execute(query)


def new_user(name, password):  # добавить нового пользователя
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''insert into User(name, password, balance) values
({name}, {password}, 0)'''
        cursor.execute(query)


def new_income(user_id, category_id, amount, date, currency, Title=None, Content=None):  # добавить новый доход
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''insert into Income(user_id, category_id, amount, date, currency, Title, Content) values
({user_id}, {category_id}, {amount}, {date.strftime('%Y-%m-%d')}, "{currency}", {'"' + Title + '"' if Title else "NULL"}, 
{'"' + Content + '"' if Content else "NULL"})'''
        cursor.execute(query)


def export():  # экспорт данных в csv-файл (пока не работает хаха)
    con = sqlite3.connect('../../DataBase/db.db')
    cursor = con.cursor()
    query = ''
    cursor.execute(query)
    row = cursor.fetchall()
    with open('output.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(row)
    cursor.close()


def set_user(id, name=None, password=None):  # поменять имя и/или пароль пользователя по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        if name:
            query = f'''UPDATE User SET name = '{name}' WHERE id = {id};'''
        if password:
            query = f'''UPDATE User SET password = '{password}' WHERE id = {id};'''
        cursor.execute(query)


def select_costs(user_id, date_from=datetime.datetime(1, 1, 1), date_to=datetime.date.today(), category_id=None, amount=None):  # выбирает расходы за определенный промежуток времени и/или по категории и/или размеру
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        if category_id:
            query = f'''select * from Costs where user_id = {user_id} and category_id = {category_id} and date(Costs.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}');'''
        else:
            query = f'''select * from Costs where user_id = {user_id} and date(Costs.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}');'''
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def select_income(user_id, date_from=datetime.datetime(1, 1, 1), date_to=datetime.date.today(), category_id=None, amount=None):  # выбирает доходы за определенный промежуток времени и/или по категории и/или размеру
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        if category_id:
            query = f'''select * from Income where user_id = {user_id} and category_id = {category_id} and date(Income.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}');'''
        else:
            query = f'''select * from Income where user_id = {user_id} and date(Income.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}'); '''
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def delete_income():
    pass


def delete_costs():
    pass


def new_category():
    pass


def delete_category():
    pass


def delete_user(id):  # удалаяет пользователя по id
    pass


def select_user(id):  # возвращает данные пользователя по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        db.row_factory = sqlite3.Row
        query = f'''select * from User where id = {id};'''
        cursor.execute(query)
        result = cursor.fetchone()
        return result
