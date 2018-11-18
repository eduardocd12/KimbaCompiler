class Quadruple():
    def __init__(self, quadruple_number, operator, left_operand, right_operand,
            result):
        self.quadruple_number = quadruple_number
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def fill_quadruple_jump(self, jump_number):
        """Updates the quadruple's result with the number of the jump"""
        self.result = jump_number

    def __str__(self):
        return (str(self.quadruple_number)  + " | " + str(self.operator) + ", "
            + str(self.left_operand) + ", " + str(self.right_operand) + ", "
            + str(self.result))
