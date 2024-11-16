# Задача "Логирование бегунов".

import unittest
import logging
import rt_with_exceptions as rtwe

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    # is_frozen = False

    # @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            tw1 = rtwe.Runner('runner_walk', -10)
            logging.info(f'"test_walk" выполнен успешно')
            tw1 = rtwe.Runner('runner_walk', -10)
            for _ in range(0, 10):
                tw1.walk()
            self.assertEqual(tw1.distance, 50)
        except:
            print("kewfbhweifb")
            logging.warning(f"Неверная скорость для Runner", exc_info=True)
            return 0

    # @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            tr1 = rtwe.Runner(7, 10)
            logging.info(f'"test_run" выполнен успешно')
            tr1 = rtwe.Runner(7, 10)
            for _ in range(0, 10):
                tr1.run()
            self.assertEqual(tr1.distance, 100)
        except:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    # @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        tw2 = rtwe.Runner('runner_walk')
        tr2 = rtwe.Runner('runner_run')
        for _ in range(0, 10):
            tw2.walk()
            tr2.run()
        self.assertNotEqual(tw2.distance, tr2.distance)


if __name__ == "__main__":
    unittest.main()
