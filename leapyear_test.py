import unittest
import leapyear


class TestCase(unittest.TestCase):
    def testDivisibleBy4(self):
        self.assertTrue(leapyear.isDivisibleBy4(4))

    def testNotDivisibleBy100(self):
        self.assertFalse(leapyear.isNotDivisibleBy100(100))
        
    def testDivisibleBy400(self):
        self.assertTrue(leapyear.isDivisibleBy400(400))
    
    def testLeapYearChecker(self):
        self.assertTrue(leapyear.leapYearChecker(2000))
    
    def finalTest(self):
        self.assertEqual(leapyear,'Leap Year')
        
if __name__ == '__main__':
    unittest.main()
