# -*- coding: utf-8 -*- 

test_list = ['python','-','ism','.','com']
print test_list

for i in test_list:
    print i

test_list.append('test1')
print test_list

test_list.insert(3,'gogo')
print test_list

test_list.remove('com')
print test_list

print test_list.index('test1')

print test_list.pop(5)
print test_list

print test_list.count('gogo')

print len(test_list)
