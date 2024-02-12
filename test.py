import unittest
from code.my_calculations import Calculations

cal = Calculations(8, 2)
print(cal.get_sum())

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculations = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculations.get_sum(), 1, "The sum is wrong.")

    def test_diff(self):
        self.assertEqual(self.calculations.get_difference(), 6, "The difference is wrong.")


if __name__ == "__main__":
    unittest.main()