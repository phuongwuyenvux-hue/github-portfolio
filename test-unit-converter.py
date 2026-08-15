import unittest
from unit_converter import convert_ounces, convert_quarts


class TestUnitConverter(unittest.TestCase):

    def test_convert_ounces(self):
        """Test fluid ounces to pints, quarts, and liters."""
        result = convert_ounces(32.0)
        self.assertEqual(result["pints"], 2.0)
        self.assertEqual(result["quarts"], 1.0)

    def test_convert_quarts(self):
        """Test quarts to pints, ounces, and liters."""
        result = convert_quarts(2.0)
        self.assertEqual(result["pints"], 4.0)
        self.assertEqual(result["ounces"], 64.0)


if __name__ == "__main__":
    unittest.main()
