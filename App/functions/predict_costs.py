import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import sqlite3
import csv
import datetime

def predict_costs(id):
    id = 1
    con = sqlite3.connect('../../DataBase/db.db')
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    # найдем минимальную дату
    format = '%Y-%m-%d'
    query = '''SELECT min(date(date, 'start of month') ) as a FROM Income WHERE user_id = 1'''
    cursor.execute(query)
    min_date = cursor.fetchone()
    min_date = datetime.datetime.strptime(min_date['a'], format)

    query = f'''SELECT sum(amount) as before,
           date(date, 'start of month') AS month
      FROM Income
     WHERE Income.user_id = {id} AND 
           CAST (strftime('%d', date) AS INT) <= {datetime.datetime.now().day} AND
           strftime('%m', date) != strftime('%m', date('now'))
     GROUP BY strftime('%m', date)
     order by date(date)
    '''
    cursor.execute(query)
    before = cursor.fetchall()
    before = [dict(item) for item in before]

    query = f'''SELECT sum(amount) as after,
           date(date, 'start of month') AS month
      FROM Costs
     WHERE user_id = {id} AND 
           CAST (strftime('%d', date) AS INT) >= {datetime.datetime.now().day} AND
           strftime('%m', date) != strftime('%m', date('now'))
     GROUP BY strftime('%m', date)
     order by date(date)
    '''
    cursor.execute(query)
    after = cursor.fetchall()
    after = [dict(item) for item in after]

    dump = list()
    for item in before:
        dump.append(item)
        a = tuple(filter(lambda elem: elem['month'] == item['month'], after))
        item.update({'after': a[0]['after'] if a else 0})
        item['month'] = (datetime.datetime.strptime(item['month'], format) - min_date).days // 31

    query = f'''SELECT sum(amount) as before,
           date(date, 'start of month') AS month
      FROM Income
     WHERE Income.user_id = {id} AND 
           CAST (strftime('%d', date) AS INT) <= {datetime.datetime.now().day} AND
           strftime('%m', date) = strftime('%m', date('now'))
    '''
    cursor.execute(query)
    current_month = dict(cursor.fetchone())
    current_month['month'] = (datetime.datetime.strptime(current_month['month'], format) - min_date).days // 31
    dump.append(current_month)
    cursor.close()

    # записываем в csv
    keys = ['month', 'before', 'after']
    with open('costs.csv', 'w', encoding='utf-8', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dump)

    # считываем данные из csv в датафрейм pandas
    data = pd.read_csv('costs.csv', sep=',')
    print(data)
    size = len(data.index)
    x = data.iloc[:size - 1].drop('after', axis=1)
    y = data.iloc[:size - 1]['after']
    last = data.iloc[size - 1].drop('after')

    # создаем модель линейной регрессии и подгоняем ее под имеющиеся данные
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    result = model.predict(np.array([[last[0], last[1]]]))
    result = float(result)

    return result

