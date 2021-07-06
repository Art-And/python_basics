import unittest


def sumy(num_1, num_2):
    return num_2 + num_1


class BlackBoxTesting(unittest.TestCase):

    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = sumy(num_1, num_2)

        self.assertEqual(result, 15)

    def test_less_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sumy(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()