import unittest
from taxtime import TaxTime

class TaxTimeTest(unittest.TestCase):
    def test_income_less_or_equal_0(self):
        tax = TaxTime()
        self.assertEqual(0, tax.taxTotal)

    def test_income_less_or_equal_9000(self):
        tax = TaxTime()
        tax.income = 9000
        tax.nFamilyMembers = 2
        print(tax.taxTotal)
        self.assertEqual(880, tax.taxTotal)
