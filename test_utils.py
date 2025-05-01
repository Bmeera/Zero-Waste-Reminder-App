import unittest
from utils import get_days_until
from datetime import datetime, timedelta

class TestUtils(unittest.TestCase):

    def test_get_days_until_future_date(self):
        future = datetime.today().date() + timedelta(days=3)
        self.assertEqual(get_days_until(future), 3)

    def test_get_days_until_today(self):
        today = datetime.today().date()
        self.assertEqual(get_days_until(today), 0)

    def test_get_days_until_past_date(self):
        past = datetime.today().date() - timedelta(days=2)
        self.assertEqual(get_days_until(past), -2)

if __name__ == '__main__':
    unittest.main()
