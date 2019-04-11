import unittest
import nose.tools as nt
import numpy as np, testing_demo as td


class Test_demo_code(unittest.TestCase):

    def setUp(self):
        self.example_arr = np.array(((3.2, 0.0), (0.0, 8.9)))
        pass

    def tearDown(self):
        pass

    def runTest(self):
        pass

    def test_rand_arr(self):
        # Test size of array
        test_arr = td.demo_code.rand_arr(4)
        nt.assert_equal(test_arr.shape, (4, 4))

    def test_hardcoded_arr(self):
        test_arr = td.demo_code.hardcoded_arr()
        self.assertAlmostEqual(test_arr[0,0], self.example_arr[0,0], places=3)

    def test_error_msg(self):
        self.assertRaises(TypeError, td.demo_code.error_msg, 4.0)
        


if __name__ == "__main__":
    unittest.main()