import unittest
from math import floor, pow
def getSmallest(n):
    n=int(floor(n))
    num_of_digits=len(str(n))-1
    if num_of_digits<1:
        return 0
    return pow(10, num_of_digits)
    




class getSmallestTest(unittest.TestCase):
    def test_less_than_ten(self):
        self.assertEqual(getSmallest(3), 0)
        self.assertEqual(getSmallest(4), 0)
        self.assertEqual(getSmallest(9.2), 0)  

    def test_less_than_hund(self):
        self.assertEqual(getSmallest(30), 10)
        self.assertEqual(getSmallest(98), 10)
        self.assertEqual(getSmallest(92.2), 10)  

    def test_less_than_thousand(self):
        self.assertEqual(getSmallest(223), 100)
        self.assertEqual(getSmallest(489), 100)
        self.assertEqual(getSmallest(928.8999), 100)  

 


if __name__ == '__main__':
    unittest.main()
