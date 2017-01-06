# -*- coding: utf-8 -*-

import sys, os
os.environ['PYTHONIOENCODING'] = 'UTF-8'

args = sys.argv

print args

print type(args[1])
print (u'引数の表示').encode('utf-8')

print (u'第１引数：' + args[1]).encode('utf-8')
print (u'第２引数：' + args[2]).encode('utf-8')
print (u'第３引数：' + args[3]).encode('utf-8')

print u'第１引数：' + args[1]
