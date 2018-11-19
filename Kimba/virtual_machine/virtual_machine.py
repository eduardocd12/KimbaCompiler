from assets.function_directory import FunctionDirectory
from virtual_machine.memory_request import MemoryRequest

import turtle

class VirtualMachine():
    def __init__(self, memory, function_directory, instructions):
        self.memory = memory
        self.function_directory = function_directory
        self.instructions = instructions
        self.number_of_instructions = len(self.instructions)
        self.instruction_counter = 0

    def run(self):
    	current_function = {}
    	parameter_position = 0
    	current_memory = self.memory
    	while self.instruction_counter < self.number_of_instructions:
            current_instruction = self.instructions[self.instruction_counter]
            operator = current_instruction.operator
            left_operand_address = current_instruction.left_operand
            right_operand_address = current_instruction.right_operand
            result_address = current_instruction.result