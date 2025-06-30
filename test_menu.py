import unittest
from project1 import menu

class TestMenuItems(unittest.TestCase):

    def test_pizza_price(self):
        self.assertEqual(menu['Pizza'], 40)

    def test_invalid_item(self):
        self.assertNotIn('Sushi', menu)

    def test_all_items_present(self):
        expected_items = ['Pizza', 'Pasta', 'Burger', 'salad', 'Coffee']
        for item in expected_items:
            self.assertIn(item, menu)

if __name__ == '__main__':
    unittest.main()
