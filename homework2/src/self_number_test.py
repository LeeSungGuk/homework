import unittest
from homework2.src import SelfNumber

class SelfNumberTest(unittest.TestCase):

    def test_전체합(self):
       self.assertEqual(SelfNumber.total_sum(1, 10), 45)


    def test_self_num_sum(self):
        # self.assertEqual(SelfNumber.self_num_total(1, 10, 45), 25)
        pass

if __name__ == '__main__':
    unittest.main()