# -*- coding: utf-8 -*-

import datetime

def get_today():
    
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
    
    return value

tuple_today = get_today()

print tuple_today
print tuple_today[0]
print tuple_today[1]
print tuple_today[2]





