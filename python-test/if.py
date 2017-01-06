# -*- coding: utf-8 -*-

value = 2

if value == 1:
    print u'valueの値は1です'
elif value == 2:
    print u'valueの値は2です'
elif value == 3:
    print u'valueの値は3です'
else:
    print u'該当する値はありません'

print '--------------------------'

value_1 = 'python'
value_2 = 'ism'

if value_1 == 'Python':
    pass
elif value_1 == 'python' and value_2 == 'ism':
    print u'2番目の条件がTrue'
elif value_1 == 'IZM' or value_2 == 'PYTHON':
    print u'3番目の条件がTrue'

