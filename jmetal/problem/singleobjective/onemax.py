import random

from jmetal.core.problem.binaryProblem import BinaryProblem
from jmetal.core.solution.binarySolution import BinarySolution

""" Class representing problem Kursawe """
__author__ = "Antonio J. Nebro"


class OneMax(BinaryProblem):
    def __init__(self, number_of_bits: int = 256):
        self.number_of_bits = number_of_bits
        self.number_of_objectives = 1
        self.number_of_variables = 1
        self.number_of_constraints = 0

    def evaluate(self, solution: BinarySolution):
        counter_of_ones = 0
        for bits in solution.variables[0]:
            if bits:
                counter_of_ones += 1

        solution.objectives[0] = -1.0 * counter_of_ones

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(number_of_variables=1, number_of_objectives=1)
        new_solution.variables[0] = \
            [True if random.randint(0, 1) == 0 else False for i in range(self.number_of_bits)]

        return new_solution

    def get_name(self):
        return "OneMax"

