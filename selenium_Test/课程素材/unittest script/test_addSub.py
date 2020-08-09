import unittest
from calculator import *

class Test_add(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)

    def test_add1(self):
        j=Math(10,20)
        self.assertEqual(j.add(),30)

    def tearDown(self):
        print("test end")

class Test_sub(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_sub(self):
        i=Math(8,8)
        self.assertEqual(i.sub(),0)

    def test_sub1(self):
        i=Math(5,3)
        self.assertEqual(i.sub(),2)

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_sub("test_sub"))
    suite.addTest(Test_sub("test_sub1"))

    runer=unittest.TextTestRunner()
    runer.run(suite)
