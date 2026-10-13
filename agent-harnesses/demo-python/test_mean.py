import unittest
from mean import mean

class MeanTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_single_value(self):
        self.assertEqual(mean([5]), 5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            mean([])

if __name__ == "__main__":
    unittest.main()
