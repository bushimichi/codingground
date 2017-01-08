# -*- coding: utf-8 -*-


print "import.py"

import testmod

tc1 = testmod.TestClass()
tc1.test_method('1')

from testmod import TestClass
tc2 = TestClass()
tc2.test_method('2')




