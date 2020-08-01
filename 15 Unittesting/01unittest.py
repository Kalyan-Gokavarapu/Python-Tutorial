import unittest

def power(a,n):
    return a**n


class MyTestClass(unittest.TestCase):
    def testpower(self):
        self.assertEquals(power(3,2),9)

# if imported as module don't execute the below
if __name__=="__main__":
    unittest.main()