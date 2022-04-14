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


def select_costs(user_id, date_from=datetime.datetime(1, 1, 1), date_to=datetime.date.today(), category_id=None, amount_from=None, amount_to=None):  # выбирает расходы за определенный промежуток времени и/или по категории и/или размеру
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        if category_id:
            query = f'''select * from Costs where user_id = {user_id} and category_id = {category_id} and date(Costs.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}');'''
        else:
            query = f'''select * from Costs where user_id = {user_id} and date(Costs.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}');'''
        if amount_from:
            query += f'''and amount between {amount_to} and {amount_from}'''
        cursor.execute(query)
        result = cursor.fetchall()
        result = [dict(item) for item in result]
        return result


def select_income(user_id, date_from=datetime.datetime(1, 1, 1), date_to=datetime.date.today(), category_id=None, amount_from=None, amount_to=None):  # выбирает доходы за определенный промежуток времени и/или по категории и/или размеру
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        if category_id:
            query = f'''select * from Income where user_id = {user_id} and category_id = {category_id} and date(Income.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}')'''
        else:
            query = f'''select * from Income where user_id = {user_id} and date(Income.date) between date('{date_from.strftime('%Y-%m-%d')}') and date('{date_to.strftime('%Y-%m-%d')}')'''
        if amount_from:
            query += f'''and amount between {amount_to} and {amount_from}'''
        cursor.execute(query)
        result = cursor.fetchall()
        result = [dict(item) for item in result]
        return result


def select_operations(user_id, n=20):
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        query = f'''select * from Costs where user_id = {user_id}'''
        cursor.execute(query)
        costs = [dict(item) for item in cursor.fetchall()]
        for item in costs:
            item.update({'type': 'cost'})
        query = f'''select * from Income where user_id = {user_id}'''
        cursor.execute(query)
        income = [dict(item) for item in cursor.fetchall()]
        for item in income:
            item.update({'type': 'income'})
        format = '%Y-%m-%d'
        result = sorted((costs + income), key=lambda item: datetime.datetime.strptime(item['date'], format))

        answer = list()
        for i in range(len(result) // n + 1):
            answer.append(result[i:i + n])
        return answer


def delete_income():  # удаляет доход по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = f'''delete from Income where id={id};'''
        cursor.execute(query)


def delete_costs():  # удаляет расход по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''delete from Costs where id={id};'''
        cursor.execute(query)


def new_category(name, colour):
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''insert into Category(name, colour) values ('{name}', '{colour}')'''
        cursor.execute(query)


def delete_category():
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''delete from Category where id={id};'''
        cursor.execute(query)


def delete_user(id):  # удалаяет пользователя по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        cursor = db.cursor()
        query = f'''delete from User where id={id};'''
        cursor.execute(query)


def select_user(id):  # возвращает данные пользователя по id
    with sqlite3.connect('../../DataBase/db.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = f'''select * from User where id = {id};'''
        cursor.execute(query)
        result = cursor.fetchone()
        return dict(result)
