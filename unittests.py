import unittest

class TestLogReg(unittest.TestCase):
    def setUp(self):
        self.x = 1
        self.y = 1
        self.z = 2

    def test_1(self):
        print("\nTesting x and z")
        print(self.x)
        print(self.z)
        self.assertNotEqual(self.x , self.z)

    def test_2(self):
        print("\nTesting y and z")
        print(self.x)
        print(self.z)
        self.assertNotEqual(self.x , self.z)

    def test_3(self):
        print("\nTesting x and z")
        print(self.x)
        print(self.y)
        self.assertAlmostEqual(self.x ,self.y)
        



if __name__ == '__main__':
    unittest.main()
