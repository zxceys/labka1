#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
} 

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
table_code = goods['Стол']
table_item = store[table_code][0]
table_item1 = store[table_code][1]
table_quantity = table_item['quantity'] + table_item1['quantity']
table_quantity1 = table_item['quantity']
table_quantity2 = table_item1['quantity']
table_price = table_item['price']
table_price1 = table_item1['price']
table_cost = table_quantity1 * table_price
table_cost1 = table_quantity2 * table_price1
table_cost2 = table_cost + table_cost1
print('Стол -', table_quantity, 'шт, стоимость', table_cost2, 'руб')

s_code = goods['Диван']
s_item = store[s_code][0]
s_item1 = store[s_code][1]
s_quantity = s_item['quantity'] + s_item1['quantity']
s_quantity1 = s_item['quantity']
s_quantity2 = s_item1['quantity']
s_price = s_item['price']
s_price1 = s_item1['price']
s_cost = s_quantity1 * s_price
s_cost1 = s_quantity2 * s_price1
s_cost2 = s_cost + s_cost1
print('Диван -', s_quantity, 'шт, стоимость', s_cost2, 'руб')

c_code = goods['Стул']
c_item = store[c_code][0]
c_item1 = store[c_code][1]
c_item2 = store[c_code][2]
c_quantity = c_item['quantity'] + c_item1['quantity'] + c_item2['quantity']
c_quantity1 = c_item['quantity']
c_quantity2 = c_item1['quantity']
c_quantity3 = c_item2['quantity']
c_price = c_item['price']
c_price1 = c_item1['price']
c_price2 = c_item2['price']
c_cost = c_quantity1 * c_price
c_cost1 = c_quantity2 * c_price1
c_cost2 = c_quantity3 * c_price2
c_cost3 = c_cost + c_cost1 + c_cost2
print('Стул -', c_quantity, 'шт, стоимость', c_cost3, 'руб')