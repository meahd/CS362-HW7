import unittest
import leapyear


class TestCase(unittest.TestCase):
    def testDivisibleBy4(self):
        self.assertTrue(leapyear.isDivisibleBy4(4))

    def testNotDivisibleBy100(self):
        self.assertFalse(leapyear.isNotDivisibleBy100(100))
    
if __name__ == '__main__':
    unittest.main()
