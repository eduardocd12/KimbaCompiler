from assets.function_directory import FunctionDirectory


class VirtualMachine():
    def __init__(self, memory, function_directory, instructions):
        self.memory = memory
        self.function_directory = function_directory
        self.instructions = instructions
        self.number_of_instructions = len(self.instructions)
        self.number_of_current_instruction = 0
