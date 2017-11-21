import unittest
from solve_puzzle import SolvePuzzle


class TestSolveSmallPuzzle(unittest.TestCase):
    def setUp(self):
        self.solutions = {'d': 72, 'e': 507, 'f': 492, 'g': 114,
                          'h': 65412, 'i': 65079, 'x': 123, 'y': 456}
        self.file = 'small_test_puzzle.txt'

    def test_solve_puzzle_d(self):
        wire = 'd'

        puzzle = SolvePuzzle(self.file)
        wire_result = puzzle.solve_puzzle(wire)

        self.assertEqual(puzzle.wire_solutions['x'], 123)
        self.assertEqual(puzzle.wire_solutions['y'], 456)

        self.assertEqual(wire_result, self.solutions[wire])

    def test_compute_all_values(self):

        for wire in self.solutions.keys():
            puzzle = SolvePuzzle(self.file)
            wire_result = puzzle.solve_puzzle(wire)
            self.assertEqual(wire_result, self.solutions[wire])


class TestSolvePuzzle(unittest.TestCase):
    def setUp(self):
        self.solutions = {'m': 510, 'n': 246, 'o': 456, 'x': 123, 'y': 456}
        self.file = 'test_2_puzzle.txt'

    def test_build_tree_all_values(self):
        for wire in self.solutions.keys():
            puzzle = SolvePuzzle(self.file)
            wire_result = puzzle.solve_puzzle(wire)
            self.assertEqual(wire_result, self.solutions[wire])


if __name__ == '__main__':
    unittest.main()
