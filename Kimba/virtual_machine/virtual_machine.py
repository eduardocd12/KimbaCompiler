from assets.function_directory import FunctionDirectory
from virtual_machine.memory_request import MemoryRequest
from ast import literal_eval

import turtle

class VirtualMachine():
    def __init__(self, memory, function_directory, instructions):
        self.memory = memory
        self.function_directory = function_directory
        self.instructions = instructions
        self.number_of_instructions = len(self.instructions)
        self.instruction_counter = 0
    def get_local_addresses(self, current_function):
        for i in range(current_function['function']['number_of_local_variables']['int']):
            current_function['memory'].get_local_address('int')
        for i in range(current_function['function']['number_of_local_variables']['float']):
            current_function['memory'].get_local_address('float')
        for i in range(current_function['function']['number_of_local_variables']['string']):
            current_function['memory'].get_local_address('string')
        for i in range(current_function['function']['number_of_local_variables']['bool']):
            current_function['memory'].get_local_address('bool')

    def get_temporal_addresses(self, current_function):
        for i in range(current_function['function']['number_of_temporal_variables']['int']):
            current_function['memory'].get_temporal_address('int')
        for i in range(current_function['function']['number_of_temporal_variables']['float']):
            current_function['memory'].get_temporal_address('float')
        for i in range(current_function['function']['number_of_temporal_variables']['string']):
            current_function['memory'].get_temporal_address('string')
        for i in range(current_function['function']['number_of_temporal_variables']['bool']):
            current_function['memory'].get_temporal_address('bool')

    def get_input_type(self, value):
        try:
            return type(literal_eval(value))
        except (ValueError, SyntaxError):
            return str

    def get_as_string(self, value):
        if self.get_type(value) is int:
            return 'int'
        elif self.get_type(value) is float:
            return 'float'
        elif self.get_type(value) is bool:
            return 'bool'
        elif self.get_type(value) is str:
            return 'string'

    def set_type(self, value):
        if self.get_type(value) is int:
            return int(value)
        elif self.get_type(value) is float:
            return float(value)
        elif self.get_type(value) is bool:
            return bool(value)
        elif self.get_type(value) is str:
            return value

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
            local_segment_pointer = []
            temporal_segment_pointer = []
            instruction_back = []

            if isinstance(left_operand_address, dict):
                left_operand_address = current_memory.get_value(left_operand_address['index_address'])
            if isinstance(right_operand_address, dict):
                right_operand_address = current_memory.get_value(right_operand_address['index_address'])
            if isinstance(result_address, dict):
                result_address = current_memory.get_value(result_address['index_address'])

            if operator == '+':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(left_operand_address)
            	result = left_operand + right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '-':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(left_operand_address)
            	result = left_operand - right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '*':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(left_operand_address)
            	result = left_operand * right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '/':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(left_operand_address)
            	if right_operand != 0:
            		if type(left_operand) == 'float' or type(right_operand) == 'float':
            			result = left_operand / right_operand
            		else:
            			result = int(left_operand/right_operand)
            	else:
            		print("Error. Division by 0")
            		sys.exit()
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == '=':
            	left_operand = current_memory.get_value(left_operand_address)
            	result = left_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '>':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand > right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '<':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand < right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1 

            elif operator == '>=':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand >= right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == '<=':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand <= right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == '==':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand == right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == '!=':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand != right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == 'and':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand and right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == 'or':
            	left_operand = current_memory.get_value(left_operand_address)
            	right_operand = current_memory.get_value(right_operand_address)
            	result = left_operand or right_operand
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == 'PRINT':
            	left_operand = current_memory.get_value(left_operand_address)
            	print(str(left_operand))
            	current_memory.set_value(result_address, result)
            	self.instruction_counter +=1

            elif operator == 'READ':
                var_type = left_operand_address
                var_input = current_memory.get_value(right_operand_address)
                input_value = input(str(var_input) + "\n")
                input_value_type = self.get_as_string(input_value)
                current_memory.set_value(result_address, result)
                self.instruction_counter +=1

            elif operator == 'GOTO':
                self.instruction_counter = result_address - 1

            elif operator == 'GOTOF':
                left_operand = current_memory.get_value(left_operand_address)
                if left_operand == False:
                    self.instruction_counter = result_address - 1
                else:
                    self.instruction_counter += 1

            elif operator == 'VERF_INDEX':
                base = current_memory.get_value(left_operand_address)
                lower_limit = right_operand_address
                upper_limit = result_address
                if base >= lower_limit and base < upper_limit:
                    self.instruction_counter += 1
                else:
                    print("Error. Index out of range")
                    sys.exit()

            elif operator == 'RETURN':
                left_operand = current_memory.get_value(left_operand_address)
                result = left_operand
                current_memory.set_value(result_address, result)
                self.instruction_counter += 1

            elif instruction_action == 'ERA':
                current_function['function'] = self.function_directory.get_function(left_operand_address)
                current_function['memory'] = Memory()
                parameter_position = 0
                self.get_local_addresses(current_function)
                self.get_temporal_addresses(current_function)

                # Pass to the next quadruple
                self.number_of_current_instruction += 1

            elif operator == 'PARAMETER':
                left_operand = current_memory.get_value(left_operand_address)
                parameter_address = current_function['function']['parameters']['addresses'][parameter_position]
                parameter_position += 1
                current_function['memory'].set_value(parameter_adress, left_operand)
                self.instruction_counter += 1

            elif operator == 'GOSUB':
                instruction_back.append(self.instruction_counter)
                local_segment_pointer.append(current_memory.local_memory)
                temporal_segment_pointer.append(current_memory.temporal_memory)
                current_memory.local_memory = current_function['memory'].local_memory
                current_memory.temporal_memory = current_function['memory'].temporal_memory
                self.instruction_counter = result_address - 1

            elif operator == 'ENDPROC':
                current_function.clear()
                current_memory.local_segment_pointer.pop()
                current_memory.temporal_segment_pointer.pop()
                self.instruction_counter = instruction_back.pop() + 1

            elif operator == 'START':
                kimba_turtle = turtle.Turtle()
                self.instruction_counter += 1

            elif operator == 'RESET':
                kimba_turtle.reset()
                self.instruction_counter += 1

            elif operator == 'END':
                kimba_turtle.done()
                self.instruction_counter += 1

            elif operator == 'SI_DIBUJA':
                kimba_turtle.pendown()
                self.instruction_counter += 1

            elif operator == 'NO_DIBUJA':
                kimba_turtle.penup()
                self.instruction_counter += 1

            elif operator == 'END':
                kimba_turtle.done()
                self.instruction_counter += 1

            elif operator == 'DIBUJA_POLIGONO':
                number_of_sides = current_memory.get_value(left_operand_address)
                size = current_memory.get_value(right_operand_address)
                rotate_angle = 360/number_of_sides
                for i in range (number_of_sides):
                    t.forward(size)
                    t.right(rotate_angle)
                    t.forward(size)
                self.instruction_counter += 1

            elif operator == 'DIBUJA_CIRCULO':
                size = current_memory.get_value(left_operand_address)
                kimba_turtle.circle(size)
                self.instruction_counter += 1

            elif operator == 'DIBUJA_ESTRELLA':
                size = current_memory.get_value(left_operand_address)
                for i in range (5):
                    star.forward(size)
                    star.right(144)
                self.instruction_counter += 1

            elif operator == 'COLOR_PLUMA':
                left_operand = current_memory.get_value(left_operand_address)
                color = left_operand
                color = color_name[1:-1]
                current_turtle.pencolor(color)




