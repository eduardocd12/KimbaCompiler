from assets.function_directory import FunctionDirectory
from assets.semantic_cube import SemanticCube
from virtual_machine.memory_request import MemoryRequest

class Code():
	def __init__(self, global_scope = "", current_scope = ""):
		self.global_scope = global_scope
		self.current_scope = current_scope
		self.memory_request = MemoryRequest()
		self.function_directory = FunctionDirectory()
		self.semantic_cube = SemanticCube()
		self.quadruple_list = []
		self.jump_list = []
		self.quadruple_number = 1
		self.temporal_variables = []
		self.temporal_parameters_names = []
		self.temporal_parameters_types = []
		self.temporal_arguments_types = []
		self.list_variable = {}
		self.operand_list = []
		self.operator_list = []
		self.type_list = []
		self.list_variable_list = []
		self.list_variable_flag = False
		self.return_flag = False
		self.return_list = []


	def print_quadruples(self):
		for quadruple in self.quadruple_list:
			print(quadruple)
