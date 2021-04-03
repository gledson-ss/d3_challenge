import unittest
from predict import Predict


class TestStringMethods(unittest.TestCase):

    def test_maximum(self):
        self.assertTrue(Predict().predict(401))


if __name__ == '__main__':
    unittest.main()
