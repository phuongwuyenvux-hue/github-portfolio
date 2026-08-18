import unittest
# Import calculation functions from your business expense tracker
from business_expense_tracker import calculate_expenses, calculate_revenue, calculate_profit_loss


class TestBusinessExpenseTracker(unittest.TestCase):

    def test_calculate_revenue(self):
        """Test revenue calculation (servings * price)."""
        revenue = calculate_revenue(servings=1000, price=5.0)
        self.assertEqual(revenue, 5000.0)

    def test_calculate_expenses(self):
        """Test total expenses calculation."""
        # Example: 1000 servings @ $1.50 cost, 208 labor hrs @ $15/hr, $1000 rent, $200 utils, $100 ad
        expenses = calculate_expenses(
            servings=1000,
            serving_cost=1.5,
            labor_hours=208.0,
            labor_rate=15.0,
            rent=1000.0,
            utilities=200.0,
            advertising=100.0
        )
        # (1000 * 1.5) + (208 * 15) + 1000 + 200 + 100 = 1500 + 3120 + 1300 = 5920
        self.assertEqual(expenses, 5920.0)

    def test_calculate_profit_loss(self):
        """Test net profit/loss calculation."""
        profit = calculate_profit_loss(revenue=5000.0, expenses=4000.0)
        self.assertEqual(profit, 1000.0)


if __name__ == "__main__":
    unittest.main()
