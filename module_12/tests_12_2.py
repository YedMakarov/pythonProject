# Задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.


import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = runner_and_tournament.Runner('Усэйн', 10)
        self.r2 = runner_and_tournament.Runner('Андрей', 9)
        self.r3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f"{key}: {cls.all_results[key]}")

    def test_race_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.r1, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")

    def test_race_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.r2, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")

    def test_race_usain_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.r1, self.r2, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")


if __name__ == "__main__":
    unittest.main()
