import sys
from solve_puzzle import SolvePuzzle


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise IOError("missing the input puzzle argument.\nexample to run:\n>> python main.py input_puzzle.txt")
    input_file = sys.argv[1]
    wire_desired = raw_input("wire: ")
    if wire_desired:

        puzzle = SolvePuzzle(input_file)
        wire_result = puzzle.solve_puzzle(wire_desired)
        print "part 1: wire value is: ", wire_result

        puzzle_2 = SolvePuzzle(input_file, part_2=str(wire_result))
        wire_result = puzzle_2.solve_puzzle(wire_desired)
        print "part 2: wire value is: ", wire_result
    else:
        raise ValueError("please enter the name of the wire")
