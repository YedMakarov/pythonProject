# Задача "Заморозка кейсов".

import unittest
import tests_12_1 as rt
import tests_12_2 as tt

suiteTT = unittest.TestSuite()
suiteTT.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.RunnerTest))
suiteTT.addTest(unittest.TestLoader().loadTestsFromTestCase(tt.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteTT)
