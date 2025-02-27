import unittest
import sample

class TestSample(unittest.TestCase):  

    def __init__(self, methodName='runTest'):  
        super().__init__(methodName)  

        # Test data 
        self.a1 = 20
        self.a2 = 'Ram'
        self.b1 = 10
        self.b2 = 0
        self.checker = sample.Operation()  # Creating the object

    def test_add(self):
        # Positive test case
        result = self.checker.add(self.a1, self.b1)
        self.assertEqual(result, 30)

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.checker.add(self.a2, self.b1)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_minus(self):
        # Positive test case
        result = self.checker.minus(self.a1, self.b1)
        self.assertEqual(result, 10)

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.checker.minus(self.a2, self.b1)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_mul(self):
        # Positive test case
        result = self.checker.mul(self.a1, self.b1)
        self.assertEqual(result, 200)

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.checker.mul(self.a2, self.b1)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

    def test_div(self):
        # Positive test case
        result = self.checker.div(self.a1, self.b1)
        self.assertEqual(result, 2)

        # Negative test case for data type
        with self.assertRaises(ValueError) as context:
            self.checker.div(self.a2, self.b1)
        self.assertEqual(str(context.exception), "Value must be either an integer or a float.")

        # Negative test case for zero division
        with self.assertRaises(ValueError):
            self.checker.div(self.a1, self.b2)

if __name__ == "__main__":
    unittest.main()
    