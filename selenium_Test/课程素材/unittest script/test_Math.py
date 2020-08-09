from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j=Math(5,10)
        # self.assertEqual(j.add(),15)
        self.assertEqual(j.add(),12)

    def test_add1(self):
        j = Math(5,10)
        self.assertNotEqual(j.add(),12)

    def assertTrue_test(self):
        j=Math(5,10)
        self.assertTrue(j.add()>10)

    def assertIn_test(self):
        self.assertIn("51zxw","hello,51zxw")
        # self.assertIn("888","hello,51zxw")

    def assetIs_test(self):
        self.assertIs("51zxw","51zxw")
        # self.assertIs("51","51zxw")

    def tearDown(self):
        print("test end")

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath("assetIs_test"))

    runer=unittest.TextTestRunner()
    runer.run(suite)

