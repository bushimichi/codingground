# -*- coding: utf-8 -*-

print "print.py"

print "python"
print "-"
print "izm"
print "com"

print "-----------------"

print "python",
print "-",
print "izm",
print "com","/path","/ok"

print "----------------"
print "Pythonの学習 : %s" % "print文の学習"

print "%d-%d-%d" % (2017,1,1)
print "{0}-{1}-{2}".format(2017,1,1)


f_obj = open('test.txt', 'w')

print >> f_obj, "python-izm.com"

