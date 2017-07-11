# coding: utf8
"""
Unit-test for general_parameters.py

import unittest
import numpy as np
from input_parameters.general_parameters import GeneralParameters
from beams.beams import Electron

class test_general_parameters(unittest.TestCase):
    def setUp(self):
        self.n_turns = 10
            
    def test_kinetic_energy_positive(self):
        # Kinetic energy must be greater or equal 0 for all turns
        general_parameters = GeneralParameters(self.n_turns, self.C, 
        self.assertTrue((general_parameters.kin_energy>=0.0).all(),

    def test_cycle_time_turn1(self):
        # Cycle_time[0] must be equal to t_rev[0]
        general_parameters = GeneralParameters(self.n_turns, self.C, 
        self.assertEqual(general_parameters.cycle_time[0],
    
    def test_ring_length_exception(self):
        # Test if 'ring length size' RuntimeError gets thrown for wrong number
        # of rf sections
        with self.assertRaisesRegex(RuntimeError,'ERROR in GeneralParameters: '
            GeneralParameters(self.n_turns, self.C, self.alpha, self.momentum, 
    def test_alpha_shape_exception(self):
        # Test if 'momentum compaction' RuntimeError gets thrown for wrong 
        # shape of alpha
        alpha = [[3.21e-4, 2.e-5, 5.e-7]]   # only one array!

        with self.assertRaisesRegex(RuntimeError,'ERROR in GeneralParameters: '
            GeneralParameters(self.n_turns, self.C, alpha, self.momentum, 
    
    def test_synchronous_data_exception(self):
        # What to do when user wants momentum programme for multiple sections?
        with self.assertRaisesRegex(RuntimeError,'ERROR in GeneralParameters: '
            GeneralParameters(self.n_turns, self.C, self.alpha, 
    def test_momentum_shape_exception(self):
        # Test if RuntimeError gets thrown for wrong shape of momentum
        momentum = 450e9 # only one momentum!
        with self.assertRaisesRegex(RuntimeError,'ERROR in GeneralParameters: '
            +'Number of sections and momentum data do not match!',
            msg = 'No RuntimeError for wrong shape of momentum!'):
            GeneralParameters(self.n_turns, self.C, self.alpha, momentum, 
                              Particle = self.particle,
                              n_sections = self.num_sections)
    
    def test_momentum_length_exception(self):
        # Test if RuntimeError gets thrown for wrong length of momentum
        # Only n_turns elements per section!
        with self.assertRaisesRegex(RuntimeError,'ERROR in GeneralParameters: '
            GeneralParameters(self.n_turns, self.C, self.alpha, self.momentum, 
    
if __name__ == '__main__':
    unittest.main()