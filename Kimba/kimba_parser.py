#
# Mauricio Cortes A00816689
# Eduardo Castro A00816926
# 04/11/2018

import sys
import ply.yacc as yacc
from kimba_lexer import tokens
from assets.code import Code
from assets.quadruples import Quadruple
from virtual_machine.virtual_machine import VirtualMachine

my_code = Code()

### PROGRAM

def p_program(p):
	'''program : PROGRAM ID program_point program_point2 SEMICOLON vars functions MAIN program_point3 block'''
	print('Syntax correct')

def p_program_point(p):
	'''program_point : '''
	quadruple = Quadruple(my_code.quadruple_number, 'GOTO', 'MAIN', None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_program_point2(p):
	'''program_point2 : '''
	my_code.global_scope = p[-2]
	my_code.current_scope = p[-2]
	my_code.function_directory.add_function(my_code.global_scope, 'void')


def p_program_point3(p):
	'''program_point3 : '''
	my_code.current_scope = p[-1]
	my_code.function_directory.add_function(my_code.current_scope, 'void')
	my_code.function_directory.set_function_quadruple_number(my_code.current_scope, my_code.quadruple_number)
	quadruple = my_code.quadruple_list[0]
	quadruple.fill_quadruple_jump(my_code.quadruple_number)





### VARS
# VAR a, b, c : int;
# VAR x[5] : int;
def p_vars(p):
    '''vars : VAR ID vars_aux COLON type vars_point SEMICOLON vars
            | VAR ID list_declaration COLON type vars_point2 SEMICOLON vars
            | empty'''

def p_vars_aux(p):
    '''vars_aux : COMMA ID vars_aux
                | empty'''
    if p[-1] is not None:
        variable_name = p[-1]
        my_code.temporal_variables.append(variable_name)

def p_list_declaration(p):
    '''list_declaration : LBRACKET var_const RBRACKET list_declaration_point'''

def p_vars_point(p):
	'''vars_point : '''
	variable_type = p[-1]
	my_code.temporal_variables.reverse()
	for variable in my_code.temporal_variables:
		variable_declared = my_code.function_directory.check_existing_variable(my_code.current_scope, variable)
		if variable_declared == False:
			if my_code.current_scope == my_code.global_scope:
				variable_address = my_code.memory_request.get_global_address(variable_type)
			else:
				variable_address = my_code.memory_request.get_local_address(variable_type)
			my_code.function_directory.add_variable_to_function(my_code.current_scope, variable_type, variable, variable_address)
	del my_code.temporal_variables[:]

# For list declarations
def p_vars_point2(p):
	'''vars_point2 : '''
	variable_type = p[-1]
	variable = my_code.list_variable
	variable_declared = my_code.function_directory.check_existing_variable(my_code.current_scope, variable['name'])
	if variable_declared == False:
		if my_code.current_scope == my_code.global_scope:
			variable_address = my_code.memory_request.get_global_address_list(variable_type, variable['upper_limit'])
		else:
			variable_address = my_code.memory_request.get_local_address_list(variable_type, variable['upper_limit'])
		variable['type'] = variable_type
		variable['memory_address'] = variable_address
		my_code.function_directory.add_list_variable_to_function(my_code.current_scope, variable)

def p_list_declaration_point(p):
	'''list_declaration_point : '''
	dimensioned_variable_name = p[-4]
	dimension_size_address = my_code.operand_list.pop()
	dimension_size = my_code.memory_request.get_value(dimension_size_address)
	dimension_type = my_code.type_list.pop()
	if dimension_type != 'int':
		print("Array indexes should be of type int")
		sys.exit()
	elif dimension_size < 1:
		print("Array dimension should be greater than 0")
		sys.exit()
	else:
		my_code.list_variable_flag = True
		my_code.list_variable = {
			'name' : dimensioned_variable_name,
			'lower_limit' : 0,
			'upper_limit' : dimension_size
		}






### EXPRESSION

def p_expression_log(p):
    '''expression_log : not expression expression_log_point
                      | not expression expression_log_point AND expression_log_point2 expression_log
                      | not expression expression_log_point OR expression_log_point2 expression_log'''

def p_expression_log_point(p):
	'''expression_log_point : '''
	if len(my_code.operator_list) > 0 and len(my_code.operand_list) > 1:
		if my_code.operator_list[-1] == 'and' or my_code.operator_list[-1] == 'or':
			solve_operation(p)

def p_expression_log_point2(p):
	'''expression_log_point2 : '''
	my_code.operator_list.append(p[-1])

def p_not(p):
    '''not : NOT
           | empty'''

def p_expression(p):
    '''expression : exp expression_point2
                  | exp GREATER_THAN expression_point exp expression_point2
                  | exp LESS_THAN expression_point exp expression_point2
                  | exp GREATER_OR_EQUAL_THAN expression_point exp expression_point2
                  | exp LESS_OR_EQUAL_THAN expression_point exp expression_point2
                  | exp EQUAL_THAN expression_point exp expression_point2
                  | exp NOT_EQUAL_THAN expression_point exp expression_point2'''

def p_expression_point(p):
	'''expression_point : '''
	my_code.operator_list.append(p[-1])

def p_expression_point2(p):
	'''expression_point2 : '''
	if len(my_code.operator_list) > 0 and len(my_code.operand_list) > 1:
		if my_code.operator_list[-1] == '>' or my_code.operator_list[-1] == '<' or my_code.operator_list[-1] == '>=' or my_code.operator_list[-1] == '<=' or my_code.operator_list[-1] == '==' or my_code.operator_list[-1] == '!=':
			solve_operation(p)

def p_exp(p):
    '''exp : term exp_point
           | term exp_point PLUS exp_point2 exp
           | term exp_point MINUS exp_point2 exp '''

def p_exp_point(p):
	'''exp_point : '''
	if len(my_code.operator_list) > 0 and len(my_code.operand_list) > 1:
		if my_code.operator_list[-1] == '+' or my_code.operator_list[-1] == '-':
			solve_operation(p)

def p_exp_point2(p):
	'''exp_point2 : '''
	my_code.operator_list.append(p[-1])

def p_term(p):
    '''term : factor term_point
            | factor term_point TIMES term_point2 term
            | factor term_point DIVIDES term_point2 term'''

def p_term_point(p):
	'''term_point : '''
	if len(my_code.operator_list) > 0 and len(my_code.operand_list) > 1:
		if my_code.operator_list[-1] == '*' or my_code.operator_list[-1] == '/':
			solve_operation(p)

def p_term_point2(p):
	'''term_point2 : '''
	my_code.operator_list.append(p[-1])

def p_factor(p):
    '''factor : LPAREN factor_point expression_log RPAREN factor_point2
              | var_const '''

def p_factor_point(p):
	'''factor_point : '''
	my_code.operator_list.append('FB')

def p_factor_point2(p):
	'''factor_point2 : '''
	my_code.operator_list.pop()


def p_var_const(p):
    '''var_const : ID var_const_point list_call
                 | CONST_INT var_const_point2
                 | CONST_FLOAT var_const_point3
                 | CONST_STRING var_const_point4
                 | boolean var_const_point5
                 | function'''

def p_var_const_point(p):
	'''var_const_point : '''
	variable = my_code.function_directory.get_function_variable(my_code.current_scope, p[-1])
	if variable is None:
		variable = my_code.function_directory.get_function_variable(my_code.global_scope, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " has not been declared")
			sys.exit()
		else:
			my_code.operand_list.append(variable['memory_address'])
			my_code.type_list.append(variable['type'])
	else:
		my_code.operand_list.append(variable['memory_address'])
		my_code.type_list.append(variable['type'])

def p_var_const_point2(p):
	'''var_const_point2 : '''
	constant_address = my_code.memory_request.check_existing_constant_value('int', int(p[-1]))
	if constant_address is None:
		constant_address = my_code.memory_request.get_constant_address('int', int(p[-1]))
	my_code.operand_list.append(constant_address)
	my_code.type_list.append('int')

def p_var_const_point3(p):
	'''var_const_point3 : '''
	constant_address = my_code.memory_request.check_existing_constant_value('float', float(p[-1]))
	if constant_address is None:
		constant_address = my_code.memory_request.get_constant_address('float', float(p[-1]))
	my_code.operand_list.append(constant_address)
	my_code.type_list.append('float')

def p_var_const_point4(p):
	'''var_const_point4 : '''
	constant_address = my_code.memory_request.check_existing_constant_value('string', str(p[-1]))
	if constant_address is None:
		constant_address = my_code.memory_request.get_constant_address('string', str(p[-1]))
	my_code.operand_list.append(constant_address)
	my_code.type_list.append('string')

def p_var_const_point5(p):
	'''var_const_point5 : '''
	if p[-1] == "True":
		constant_address = my_code.memory_request.check_existing_constant_value('boolean', True)
		if constant_address is None:
			constant_address = my_code.memory_request.get_constant_address('boolean', True)
		my_code.operand_list.append(constant_address)
		my_code.type_list.append('boolean')
	else:
		constant_address = my_code.memory_request.check_existing_constant_value('boolean', False)
		if constant_address is None:
			constant_address = my_code.memory_request.get_constant_address('boolean', False)
		my_code.operand_list.append(constant_address)
		my_code.type_list.append('boolean')

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = p[1]

### RETURN

def p_return(p):
	'''return : RETURN expression_log SEMICOLON return_point'''

def p_return_point(p):
	'''return_point : ''' 
	my_code.return_flag = True
	operand = my_code.operand_list.pop()
	operand_type = my_code.type_list.pop()
	function = my_code.function_directory.get_function(my_code.current_scope)
	function_type = function['return_type']
	function_return_address = function['return_address']

	if function_type != operand_type:
		print("Return type of function {0} doesn't match function return type".format(my_code.current_scope))
		sys.exit()

	quadruple = Quadruple(my_code.quadruple_number, 'RETURN', operand, None, function_return_address)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

	quadruple = Quadruple(my_code.quadruple_number, 'GOTO', None, None, None)
	my_code.return_list.append(my_code.quadruple_number)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1



### FUNCTIONS

def p_functions(p):
    '''functions : FUNC type_func ID LPAREN params RPAREN functions_point block functions_point2 functions
                 | empty'''

def p_type_func(p):
    '''type_func : type
                 | VOID'''
    p[0] = p[1]

def p_params(p):
    '''params : type ID params_aux
              | empty'''

def p_params_aux(p):
    '''params_aux : COMMA type ID params_aux
                  | empty'''
    if p[-1] is not None:
	    parameter_name = p[-1]
	    parameter_type = p[-2]
	    my_code.temporal_parameters_names.insert(0, parameter_name)
	    my_code.temporal_parameters_types.insert(0, parameter_type)

def p_functions_point(p):
	'''functions_point : '''

	my_code.current_scope = p[-4]
	function_type = p[-5]
	parameter_addresses_list = []

	my_code.function_directory.add_function(my_code.current_scope, function_type)

	my_code.function_directory.set_function_quadruple_number(my_code.current_scope, my_code.quadruple_number)
	if function_type != 'void':
		function_address = my_code.memory_request.get_global_address(function_type)
		my_code.function_directory.set_function_address(my_code.current_scope, function_address)

	parameters = zip(my_code.temporal_parameters_names, my_code.temporal_parameters_types)

	for parameter_name, parameter_type in parameters:
		parameter_address = my_code.memory_request.get_local_address(parameter_type)
		parameter_addresses_list.append(parameter_address)
		my_code.function_directory.add_variable_to_function(my_code.current_scope, parameter_type, parameter_name, parameter_address)

	my_code.function_directory.add_parameter_to_function(my_code.current_scope, my_code.temporal_parameters_types, parameter_addresses_list)

	del my_code.temporal_parameters_names[:]
	del my_code.temporal_parameters_types[:]

def p_functions_point2(p):
	'''functions_point2 : '''
	function_type = p[-7]

	if function_type == 'void' and my_code.return_flag:
		print('Function {0} of type void should not have return statement.'.format(my_code.current_scope))
		sys.exit()
	elif function_type != 'void' and not my_code.return_flag:
		print('Function {0} of type {1} should have return statement.'.format(my_code.current_scope, function_type))
		sys.exit()
	else:
		quadruple = Quadruple(my_code.quadruple_number, 'ENDFUNC', None, None, None)
		my_code.quadruple_list.append(quadruple)

	if my_code.return_flag:
		while my_code.return_list:
			quadruple_number_to_fill = my_code.return_list.pop()
			my_code.quadruple_list[quadruple_number_to_fill - 1].fill_quadruple_jump(my_code.quadruple_number)
	my_code.quadruple_number += 1
	my_code.return_flag = False

	my_code.current_scope = my_code.global_scope
	my_code.memory_request.restart_memory()

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING
            | BOOLEAN'''
    p[0] = p[1]


### BLOCK

def p_block(p):
    '''block : LBRACE statements RBRACE'''

### STATEMENT

def p_statements(p):
    '''statements : vars statement statements
                  | vars empty'''

def p_statement(p):
    '''statement : assignment
                 | condition
                 | write
                 | loop
                 | method
                 | predefined_method
                 | return '''

### ASSIGNMENT

def p_assignment(p):
    '''assignment : ID assignment_point list_call ASSIGN assignment_point2 expression_log SEMICOLON assignment_point4
				  | ID assignment_point list_call ASSIGN assignment_point2 READ LPAREN expression_log RPAREN assignment_point3 SEMICOLON assignment_point4'''

def p_assignment_point(p):
	'''assignment_point : '''
	variable = my_code.function_directory.get_function_variable(my_code.current_scope, p[-1])
	if variable is None:
		variable = my_code.function_directory.get_function_variable(my_code.global_scope, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " has not been declared")
			sys.exit()
		else:
			my_code.operand_list.append(variable['memory_address'])
			my_code.type_list.append(variable['type'])
	else:
		my_code.operand_list.append(variable['memory_address'])
		my_code.type_list.append(variable['type'])

def p_assignment_point2(p):
	'''assignment_point2 : '''
	my_code.operator_list.append(p[-1])

def p_assignment_point3(p):
	'''assignment_point3 : '''
	received_input_address = my_code.operand_list.pop()
	my_code.type_list.pop()
	variable_type = my_code.type_list[-1]
	assignation_address = my_code.memory_request.get_temporal_address(variable_type)

	my_code.operand_list.append(assignation_address)
	my_code.type_list.append(variable_type)
	quadruple = Quadruple(my_code.quadruple_number, 'READ', variable_type, received_input_address, assignation_address)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_assignment_point4(p):
	'''assignment_point4 : '''
	operator = my_code.operator_list.pop()
	if operator == '=':
		right_operand = my_code.operand_list.pop()
		right_type = my_code.type_list.pop()
		left_operand = my_code.operand_list.pop()
		left_type = my_code.type_list.pop()
		result_type = my_code.semantic_cube.get_semantic_type(left_type, right_type, operator)
		if result_type != 'error':
			quadruple = Quadruple(my_code.quadruple_number, operator, right_operand, None, left_operand)

			my_code.quadruple_list.append(quadruple)
			my_code.quadruple_number += 1
		else:
			print('Operation type mismatch at {0}'.format(p.lexer.lineno))
			sys.exit()



### LIST CALL

def p_list_call(p):
    '''list_call : LBRACKET list_point list_point2 exp list_point3 list_point4 RBRACKET
            	 | empty'''

def p_list_point(p):
	'''list_point : '''
	variable_name = p[-3]
	my_code.operand_list.pop()
	variable = my_code.function_directory.get_function_variable(my_code.current_scope, variable_name)
	if variable is None:
		variable = my_code.function_directory.get_function_variable(my_code.global_scope, variable_name)
		if variable is None:
			print("The variable " + variable_name + " has not been declared")
			sys.exit()
		else:
			if 'upper_limit' in variable:
				my_code.list_variable_list.append(variable)
			else:
				print("The variable " + variable_name + " is not an array")
				sys.exit()
	else:
		if 'upper_limit' in variable:
			my_code.list_variable_list.append(variable)
		else:
			print("The variable " + variable_name + " is not an array")
			sys.exit()

def p_list_point2(p):
	'''list_point2 : '''
	my_code.operator_list.append('FB')

def p_list_point3(p):
	'''list_point3 : '''
	index_address = my_code.operand_list.pop()
	index_type = my_code.type_list.pop()
	dimensioned_variable = my_code.list_variable_list.pop()
	if index_type != 'int':
		print("Array indexes should be of type int")
		sys.exit()
	else:
		quadruple = Quadruple(my_code.quadruple_number, 'VERF_INDEX', index_address, dimensioned_variable['lower_limit'], dimensioned_variable['upper_limit'])
		my_code.quadruple_list.append(quadruple)
		my_code.quadruple_number += 1
		base_address_proxy = my_code.memory_request.get_global_address('int', dimensioned_variable['memory_address'])
		index_address_result = my_code.memory_request.get_global_address('int')
		quadruple = Quadruple(my_code.quadruple_number, '+', base_address_proxy, index_address, index_address_result)
		my_code.quadruple_list.append(quadruple)
		my_code.quadruple_number += 1
		result_proxy = {'index_address' : index_address_result}
		my_code.operand_list.append(result_proxy)
		my_code.type_list.append(dimensioned_variable['type'])

def p_list_point4(p):
	'''list_point4 : '''
	my_code.operator_list.pop()

### CONDITION

def p_condition(p):
    '''condition : IF LPAREN expression_log RPAREN condition_point block else condition_point2'''

def p_condition_point(p):
    '''condition_point : '''
    create_conditional_quadruple(p)

def p_condition_point2(p):
    '''condition_point2 : '''
    quadruple_number_to_fill = my_code.jump_list.pop()
    quadruple = my_code.quadruple_list[quadruple_number_to_fill]

    quadruple.fill_quadruple_jump(my_code.quadruple_number)

def p_else(p):
	'''else : ELSE else_point block
	        | empty'''

def p_else_point(p):
    '''else_point : '''
    quadruple = Quadruple(my_code.quadruple_number, 'GOTO', None, None, None)
    my_code.quadruple_list.append(quadruple)

    quadruple_number_to_fill = my_code.jump_list.pop()
    quadruple = my_code.quadruple_list[quadruple_number_to_fill]

    my_code.jump_list.append(my_code.quadruple_number - 1)
    my_code.quadruple_number += 1

    quadruple.fill_quadruple_jump(my_code.quadruple_number)

### WRITE

def p_write(p):
    '''write : PRINT LPAREN expression_log write_point RPAREN SEMICOLON'''

def p_write_point(p):
    '''write_point : '''
    operand = my_code.operand_list.pop()
    quadruple = Quadruple(my_code.quadruple_number, 'PRINT', operand, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

### LOOP

def p_loop(p):
    '''loop : WHILE loop_point LPAREN expression_log RPAREN loop_point2 block loop_point3'''

def p_loop_point(p):
    '''loop_point : '''
    my_code.jump_list.append(my_code.quadruple_number)

def p_loop_point2(p):
    '''loop_point2 : '''
    create_conditional_quadruple(p)

def p_loop_point3(p):
    '''loop_point3 : '''
    quadruple_number_to_fill = my_code.jump_list.pop()
    quadruple_number_to_return = my_code.jump_list.pop()

    while_quadruple = Quadruple(my_code.quadruple_number, 'GOTO', None, None, quadruple_number_to_return)
    my_code.quadruple_list.append(while_quadruple)
    my_code.quadruple_number += 1

    conditional_quadruple = my_code.quadruple_list[quadruple_number_to_fill]
    conditional_quadruple.fill_quadruple_jump(my_code.quadruple_number)

### METHOD

def p_method(p):
	'''method : ID LPAREN method_point method_point2 args RPAREN method_point3 method_point4 method_point5 SEMICOLON'''

def p_method_point(p):
    '''method_point : '''
    my_code.operator_list.append('FB')

def p_method_point2(p):
    '''method_point2 : '''
    function = p[-3]
    if my_code.function_directory.search_function(function):
        quadruple = Quadruple(my_code.quadruple_number, 'ERA', function, None, None)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1

        parameters = my_code.function_directory.get_function_parameters(function)
        my_code.temporal_arguments_types = list(parameters['types'])
    else:
        print("The function " + function + " you are trying to call doesn't exists")
        sys.exit()

def p_method_point3(p):
    '''method_point3 : '''
    my_code.operator_list.pop()

def p_method_point4(p):
    '''method_point4 : '''
    if not my_code.temporal_arguments_types:
        # Retrieves the function and is quadruple number
        function = p[-7]
        function_quadruple_number = my_code.function_directory.get_function_quadruple_number(function)

        quadruple = Quadruple(my_code.quadruple_number, 'GOSUB', function, None, function_quadruple_number)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1
    else:
        print('Argument number mismatch at {0} line '.format(p.lexer.lineno))
        sys.exit()

def p_method_point5(p):
    '''method_point5 : '''
    function = p[-8]
    function_type = my_code.function_directory.get_function_type(function)

    if function_type != 'void':
        print("This function {0} can't be called as a procedure".format(function))
        sys.exit()

### FUNCTION

def p_function(p):
	'''function : ID LPAREN function_point function_point2 args RPAREN function_point3 function_point4 function_point5 '''

def p_function_point(p):
    '''function_point : '''
    my_code.operator_list.append('FB')


def p_function_point2(p):
    '''function_point2 : '''
    function = p[-3]
    if my_code.function_directory.search_function(function):
        quadruple = Quadruple(my_code.quadruple_number, 'ERA', function, None, None)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1

        parameters = my_code.function_directory.get_function_parameters(function)
        my_code.temporal_arguments_types = list(parameters['types'])
    else:
        print("The function " + function + " you are trying to call doesn't exists")
        sys.exit()

def p_function_point3(p):
    '''function_point3 : '''
    my_code.operator_list.pop()

def p_function_point4(p):
    '''function_point4 : '''
    if not my_code.temporal_arguments_types:
        function = p[-7]
        function_quadruple_number = my_code.function_directory.get_function_quadruple_number(function)

        quadruple = Quadruple(my_code.quadruple_number, 'GOSUB', function,
            None, function_quadruple_number)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1
    else:
        print('Argument number mismatch at {0} line '.format(p.lexer.lineno))
        sys.exit()

def p_function_point5(p):
    '''function_point5 : '''
    function_called = p[-8]
    function = my_code.function_directory.get_function(function_called)
    function_return = function['return_address']
    function_type = function['return_type']

    #my_code.temporal_variable_counter += 1

    temporal_variable_address = my_code.memory_request.get_temporal_address(function_type)
    my_code.function_directory.add_temporal_to_function(my_code.current_scope, function_type)

    quadruple = Quadruple(my_code.quadruple_number, '=', function_return, None, temporal_variable_address)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

    my_code.operand_list.append(temporal_variable_address)
    my_code.type_list.append(function_type)


### ARGUMENTS

def p_args(p):
	'''args : expression_log args_point args_aux
			| empty'''

def p_args_aux(p):
	'''args_aux : COMMA expression_log args_point args_aux
                | empty'''

def p_args_point(p):
    '''args_point : '''
    if my_code.temporal_arguments_types:
        argument = my_code.operand_list.pop()
        argument_type = my_code.type_list.pop()
        parameter_type = my_code.temporal_arguments_types.pop(0)

        if argument_type == parameter_type:
            quadruple = Quadruple(my_code.quadruple_number, 'PARAMETER', argument, None, None)
            my_code.quadruple_list.append(quadruple)
            my_code.quadruple_number += 1
        else:
            print('Argument type mismatch at {0} line '.format(p.lexer.lineno))
            sys.exit()
    else:
        print('Agument number mismatch at {0} line '.format(p.lexer.lineno))
        sys.exit()

### VAR STRING

def p_string_var(p):
    '''string_var : ID string_var_point string_var_point2
                  | CONST_STRING string_var_point3'''


def p_string_var_point(p):
	'''string_var_point : '''
	variable = my_code.function_directory.get_function_variable(my_code.current_scope, p[-1])
	if variable is None:
		variable = my_code.function_directory.get_function_variable(my_code.global_scope, p[-1])
		if variable is None:
			print("The variable " + p[-1] + " has not been declared")
			sys.exit()
		else:
			my_code.operand_list.append(variable['memory_address'])
			my_code.type_list.append(variable['type'])
	else:
		my_code.operand_list.append(variable['memory_address'])
		my_code.type_list.append(variable['type'])
	

def p_string_var_point2(p):
	'''string_var_point2 : '''
	variable = p[-2]
	variable_type = my_code.type_list[-1]
	if variable_type != 'string':
		print("The variable: " + variable + " is not a string")
		sys.exit()   

def p_string_var_point3(p):
	'''string_var_point3 : '''  
	constant_address = my_code.memory_request.check_existing_constant_value('string', str(p[-1]))
	if constant_address is None:
		constant_address = my_code.memory_request.get_constant_address('string', str(p[-1]))
	my_code.operand_list.append(constant_address)
	my_code.type_list.append('string')


### EMPTY

def p_empty(p):
    '''empty : '''

### Funciones predefinidas

def p_predefined_function_call(p):
    '''predefined_method : START LPAREN RPAREN SEMICOLON
                         | RESET LPAREN RPAREN SEMICOLON
                         | END LPAREN RPAREN SEMICOLON
                         | GIRA_IZQ LPAREN exp RPAREN SEMICOLON
                         | GIRA_DER LPAREN exp RPAREN SEMICOLON
                         | CAMINA LPAREN exp RPAREN SEMICOLON
                         | SI_DIBUJA LPAREN RPAREN SEMICOLON
                         | NO_DIBUJA LPAREN RPAREN SEMICOLON
                         | DIBUJA_POLIGONO LPAREN exp COMMA exp RPAREN SEMICOLON
                         | DIBUJA_CIRCULO LPAREN exp RPAREN SEMICOLON
                         | DIBUJA_ESTRELLA LPAREN exp RPAREN SEMICOLON
                         | COLOR_PLUMA LPAREN string_var RPAREN SEMICOLON'''

### Funcion error

def p_error(p):
	print('Syntax error at {0}'.format(p))
	sys.exit()


### Other functions

def create_conditional_quadruple(p):
    quadruple = Quadruple(my_code.quadruple_number, 'GOTOF', None, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.jump_list.append(my_code.quadruple_number - 1)
    my_code.quadruple_number += 1


def solve_operation(p):
    """Solve an operation from the lists"""
    right_operand = my_code.operand_list.pop()
    right_type = my_code.type_list.pop()
    left_operand = my_code.operand_list.pop()
    left_type = my_code.type_list.pop()
    operator = my_code.operator_list.pop()
    result_type = my_code.semantic_cube.get_semantic_type(left_type ,
        right_type, operator)
    if result_type != 'error':
        temporal_variable_address = my_code.memory_request.get_temporal_address(result_type)
        my_code.function_directory.add_temporal_to_function(my_code.current_scope,
            result_type)
        quadruple = Quadruple(my_code.quadruple_number, operator, left_operand,
            right_operand , temporal_variable_address)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1
        my_code.operand_list.append(temporal_variable_address)
        my_code.type_list.append(result_type)
    else:
        print('Operation type mismatch at {0}'.format(p.lexer.lineno))
        sys.exit()

# Parser
parser = yacc.yacc()
with open("archivo_entrada.txt") as file_object:
    code = file_object.read()
    parser.parse(code)
my_code.print_quadruples()
vm = VirtualMachine(my_code.memory_request, my_code.function_directory, my_code.quadruple_list)
vm.run()