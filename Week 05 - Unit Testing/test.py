import unittest
import calc

class TestCalc(unittest.TestCase):
    # Creating the method to test add
    def test_add(self):
        # Saving the add function's result
        result = calc.add(10, 5)
        # assertEqual's 1st argument is the result and 2nd argument is the expected result
        self.assertEqual(result, 15)

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)