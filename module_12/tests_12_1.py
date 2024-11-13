# Задача "Проверка на выносливость"
# Цель: приобрести навык создания простейших Юнит-тестов

import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        tw1 = runner.Runner('runner_walk')
        # print(tw1.name)
        for _ in range(0, 10):
            tw1.walk()
        # print(tw1.distance)
        self.assertEqual(tw1.distance, 50)

    def test_run(self):
        tr1 = runner.Runner('runner_run')
        # print(tr1.name)
        for _ in range(0, 10):
            tr1.run()
        # print(tr1.distance)
        self.assertEqual(tr1.distance, 100)

    def test_challenge(self):
        tw2 = runner.Runner('runner_walk')
        tr2 = runner.Runner('runner_run')
        for _ in range(0, 10):
            tw2.walk()
            tr2.run()
        self.assertNotEqual(tw2.distance, tr2.distance)


if __name__ == "__main__":
    unittest.main()
