import unittest
import mean_var_std
import numpy as np

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])
        expected = {
            'mean': [[3.0, 4.0, 5.0],
                     [1.0, 4.0, 7.0],
                     4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666666666666,
                          0.6666666666666666,
                          0.6666666666666666],
                         6.666666666666667],
            'standard deviation': [[2.449489742783178,
                                    2.449489742783178,
                                    2.449489742783178],
                                   [0.816496580927726,
                                    0.816496580927726,
                                    0.816496580927726],
                                   2.581988897471611],
            'max': [[6, 7, 8],
                    [2, 5, 8],
                    8],
            'min': [[0, 1, 2],
                    [0, 3, 6],
                    0],
            'sum': [[9, 12, 15],
                    [3, 12, 21],
                    36]
        }
        for key in expected:
            self.assertAlmostEqual(actual[key][2], expected[key][2], places=10, msg=f"{key} no coincide (flattened)")
            self.assertTrue(np.allclose(actual[key][0], expected[key][0]), f"{key} no coincide (axis=0)")
            self.assertTrue(np.allclose(actual[key][1], expected[key][1]), f"{key} no coincide (axis=1)")

    def test_calculate_with_error(self):
        with self.assertRaises(ValueError) as context:
            mean_var_std.calculate([2,6,2,8,4,0,1])
        self.assertEqual(str(context.exception), "La lista debe contener nueve números")

if __name__ == "__main__":
    unittest.main()
