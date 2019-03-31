import unittest

from repo.repo import Repo


class MyTestCase(unittest.TestCase):

    def tearDown(self):
        with open("test_evolve2", "w") as f:
            f.write("")


    def test_something(self):
        repo = Repo("test_evolve")
        self.__grid = repo.get_current_element()
        print(self.__grid)
        grid = [[1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__grid.get_grid(), grid)
        self.__grid.evolve()
        repo.write_to_file("test_evolve2")
        self.__grid = repo.get_current_element()
        grid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__grid.get_grid(), grid)


if __name__ == '__main__':
    unittest.main()
