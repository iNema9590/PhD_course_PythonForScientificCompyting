import sys

import unittest

sys.path.append('../')

from lorenz import solver


class OdeSolverTester(unittest.TestCase):
    """
    OdeSolverTester class to test the desired functionalities of each method in OdeSolver class
    """


    def test_to_set_interval(self):
        obj = solver.OdeSolver(1, 2, 3)
        obj.set_time_interval(10)
        self.assertEqual(obj.get_time_interval(), 10)

    def test_to_get_time_interval(self):
        obj = solver.OdeSolver(1, 2, 3)
        self.assertEqual(obj.get_time_interval(), 0.02)

    def test_to_set_num_of_steps(self):
        obj = solver.OdeSolver(1, 2, 3)
        obj.set_num_of_steps(10)
        self.assertEqual(obj.get_num_of_steps(), 10)

    def test_to_get_num_of_steps(self):
        obj = solver.OdeSolver(1, 2, 3)
        self.assertEqual(obj.get_num_of_steps(), 10000)

    def test_simulator(self):
        obj = solver.OdeSolver(10, 2.5, 16)
        obj.set_num_of_steps(2)
        print("Simulation")
        result = obj.simulator(1, 1, 1)
        xyz_dict = dict()
        xyz_dict['x_val'] = [1, 1.0]
        xyz_dict['y_val'] = [1, 1.28]
        xyz_dict['z_val'] = [1, 0.97]
        print(result)

        self.assertEqual(result, xyz_dict)


if __name__ == '__main__':
    unittest.main()
