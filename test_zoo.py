import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(-4), 0)
       
    # Add your additional test cases here.

    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)

    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(17), 100)

    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(52), 150)

    def test_child_ticket_price5(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()