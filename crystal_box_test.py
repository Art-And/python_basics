import unittest

def if_is_greater_than_18(age):
    if age >= 18:
        return True
    else:
        return False


class CrystalBoxTest(unittest.TestCase):
    def test_if_is_greater_than_18(self):
        age = 20

        result = if_is_greater_than_18(age)

        self.assertEqual(result, True)

    def test_if_is_lees_than_18(self):
        age = 15

        result = if_is_greater_than_18(age)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()