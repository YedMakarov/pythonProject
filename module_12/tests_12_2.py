# Задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.


import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.all_results1 = {}
        cls.all_results2 = {}
        cls.all_results3 = {}

    def setUp(self):
        self.r1 = rat.Runner('Усэйн', 10)
        self.r2 = rat.Runner('Андрей', 9)
        self.r3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        all_results = {}
        for key in sorted(cls.all_results1.keys()):
            all_results[key] = f"{cls.all_results1[key]}"
        print(all_results)

        all_results = {}
        for key in sorted(cls.all_results2.keys()):
            all_results[key] = f"{cls.all_results2[key]}"
        print(all_results)

        all_results = {}
        for key in sorted(cls.all_results3.keys()):
            all_results[key] = f"{cls.all_results3[key]}"
        print(all_results)


    def test_race_usain_and_nick(self):
        tournament = rat.Tournament(90, self.r1, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        self.all_results1.update(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")

    def test_race_andrey_and_nick(self):
        tournament = rat.Tournament(90, self.r2, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        self.all_results2.update(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")

    def test_race_usain_andrey_and_nick(self):
        tournament = rat.Tournament(90, self.r1, self.r2, self.r3)
        results = tournament.start()
        self.all_results.update(results)
        # print(results)

        self.all_results3.update(results)

        last_runner_name = max(results.keys())
        self.assertTrue(results[last_runner_name] == "Ник")
