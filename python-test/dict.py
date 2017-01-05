# -*- coding: utf-8 -*-

test_dict = {"name":"yamada", "kana":"taro"}

print test_dict

for i in test_dict:
    print i
    print test_dict[i]
    

print test_dict.get('name')
print test_dict.get('age', 10)


test_dict['age'] = 200
print test_dict

del test_dict['name']
print test_dict

print test_dict.keys()
print test_dict.values()


