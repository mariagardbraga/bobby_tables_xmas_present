class SolvePuzzle:
    def __init__(self, input_puzzle_file, part_2=None):
        self.wire_solutions = dict()
        self.input_puzzle = dict()
        self.read_input_puzzle(input_puzzle_file)
        if part_2:
            self.input_puzzle['b'] = [part_2]

    def solve_puzzle(self, wire):
        """
        this is a recursive function that will solve the problem
        :param wire: value to be computed
        :return: value assigned to the wire specified in the parameter
        """

        if wire in self.wire_solutions:
            return self.wire_solutions[wire]

        elif wire.isdigit():
            return int(wire)

        else:
            wire_op = self.input_puzzle[wire]

            if len(wire_op) == 1:
                self.wire_solutions[wire] = self.solve_puzzle(wire_op[0])

            elif 'NOT' in wire_op:
                self.wire_solutions[wire] = (~self.solve_puzzle(wire_op[1])) % 65536

            elif 'AND' in wire_op:
                self.wire_solutions[wire] = self.solve_puzzle(wire_op[0]) & self.solve_puzzle(wire_op[2])

            elif 'OR' in wire_op:
                self.wire_solutions[wire] = self.solve_puzzle(wire_op[0]) | self.solve_puzzle(wire_op[2])

            elif 'LSHIFT' in wire_op:
                self.wire_solutions[wire] = self.solve_puzzle(wire_op[0]) << self.solve_puzzle(wire_op[2])

            elif 'RSHIFT' in wire_op:
                self.wire_solutions[wire] = self.solve_puzzle(wire_op[0]) >> self.solve_puzzle(wire_op[2])

            return self.wire_solutions[wire]

    def read_input_puzzle(self, filename):
        """
        This is an auxiliary method to read a given input puzzle. each line must have an operation and an assignment.
        example of input line: a AND b -> x
        :param filename: the name of the input puzzle file
        :return dict_wires: a dictionary where the keys are the assigned variable and the values are lists of the
        operation parsed.
        """

        with open(filename, 'r') as f:
            for line in f:
                list_key_value = line.strip().split('->')
                ops = list_key_value[0].strip().split(' ')
                self.input_puzzle[list_key_value[1].strip()] = ops
