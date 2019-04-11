import unittest
import nose.tools as nt
import numpy as np, demo_code as dc


class Test_demo_code(unittest.TestCase):

    def setUp(self):
        example_arr = np.array(((3.2, 0.0), (0.0, 8.9)))
        pass

    def tearDown(self):
        pass

    def runTest(self):
        pass

    def test_rand_arr(self):
        # Test size of array
        test_arr = dc.rand_arr(4)
        nt.assert_equal(test_arr.shape, (4, 4))
        


if __name__ == "__main__":
    unittest.main()