import unittest
from homework1.src import Calculator as cal


class TestCalculator(unittest.TestCase):

    def test_계산(self):
        self.assertEqual(cal.cal(["1", "*", "4", "+", "5"]), 9)
        # 내장 함수 이용하여 값이 같은 지 판단
        self.assertEqual(cal.cal(["1", "*", "4", "+", "5"]), cal.inner_fnc("1 * 4 + 5"))


if __name__ == '__main__':
    unittest.main()