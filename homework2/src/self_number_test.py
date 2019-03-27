import unittest
from homework2.src import self_number


class SelfNumberTest(unittest.TestCase):

    def test_list_num(self):
        self.assertEqual({1,2,3}, self_number.number_list(1,4))

    def test_sum_of_digits(self):
        self.assertEqual(self_number.sum_of_digits(1, 10), 90)
        self.assertEqual(self_number.sum_of_digits(1,11), 90)

    def test_sum_of_total(self):
        self.assertEqual(self_number.self_num_total(1, 5000), 1135243)

if __name__ == '__main__':
    unittest.main()