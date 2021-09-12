import unittest
import os

import computestatsrefactor

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'random_nums')


class TestComputeRefactor(unittest.TestCase):
    def setUp(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

    def tearDown(self):
        self.testfile.close()

    def test_read_ints(self):
        self.expected_filename = 'random_nums'
        self.split_filename = TESTDATA_FILENAME
        self.actual_filename = self.split_filename.split('\\')[-1]
        self.assertEqual(self.expected_filename, self.actual_filename)

    def test_standard_deviation(self):
        pass

    def test_count(self):
        len_file = len(self.testdata)
        self.actual = len_file
        self.expected = 3893
        self.assertEqual(self.expected, self.actual)

    def test_summation(self):
        self.actual = sum(computestatsrefactor.read_ints())
        self.expected = 499498
        self.assertEqual(self.actual, self.expected)


if __name__ == "__main__":
    unittest.main()
