# -*- coding: utf-8 -*-

print "test while.py"

counter = 0

while counter < 10:
    print counter
    counter += 1

counter = 0

while True:
    print counter
    if counter > 10:
        break
    counter += 1

