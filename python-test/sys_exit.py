# -*- coding: utf-8 -*-

import sys

for i in range(100):
    print i
    
    if i == 10:
        print u'10に達したので終了します'
        sys.exit()
        