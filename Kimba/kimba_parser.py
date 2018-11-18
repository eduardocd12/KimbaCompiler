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
	# Create and add quadruple main
	quadruple = Quadruple(my_code.quadruple_number, 'GOTO', 'MAIN', None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_program_point2(p):
	'''program_point2 : '''
	# Add global function name to directory
	my_code.global_scope = p[-2]
	my_code.current_scope = p[-2]
	my_code.function_directory.add_function(my_code.global_scope, 'void')


def p_program_point3(p):
	'''program_point3 : '''
	# Adds the main function to the directory, the index of the quadruple of the main function
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
    # Stores the variables found in a temporal list
    if p[-1] is not None:
        variable_name = p[-1]
        my_code.temporal_variables.append(variable_name)

def p_list_declaration(p):
    '''list_declaration : LBRACKET var_const RBRACKET list_declaration_point'''

def p_vars_point(p):
	'''vars_point : '''
	variable_type = p[-1]
	my_code.temporal_variables.reverse()
	# Adds all the variables declared in the line to the function
	for variable in my_code.temporal_variables:
		variable_declared = my_code.function_directory.check_existing_variable(my_code.current_scope, variable)
		if variable_declared == False:
			# Request the addresses depending of the scope
			if my_code.current_scope == my_code.global_scope:
				variable_address = my_code.memory.get_global_address(variable_type)
			else:
				variable_address = my_code.memory.get_local_address(variable_type)
			my_code.function_directory.add_variable_to_function(my_code.current_scope, variable_type, variable, variable_address)
	# Clears the list of temporal variables to start a new line of declarations
	del my_code.temporal_variables[:]

# For list declarations
def p_vars_point2(p):
	'''vars_point2 : '''
	variable_type = p[-1]
	variable = my_code.list_variable
	variable_declared = my_code.function_directory.check_existing_variable(my_code.current_scope, variable['name'])
	if variable_declared == False:
		# Request the addresses needed for the variable
		if my_code.current_scope == my_code.global_scope:
			variable_address = my_code.memory.get_global_address_list(variable_type, variable['upper_limit'])
		else:
			variable_address = my_code.memory.get_local_address_list(variable_type, variable['upper_limit'])
		variable['type'] = variable_type
		variable['memory_address'] = variable_address
		my_code.function_directory.add_list_variable_to_function(my_code.current_scope, variable)

def p_list_declaration_point(p):
	'''list_declaration_point : '''
	dimensioned_variable_name = p[-4]
	dimension_size_address = my_code.operand_list.pop()
	dimension_size = my_code.memory.get_value(dimension_size_address)
	dimension_type = my_code.type_list.pop()
	# Verifies the dimension of the variable
	if dimension_type != 'int':
		print("Array indexes should be of type int")
		sys.exit()
	elif dimension_size < 1:
		print("Array dimension should be greater than 0")
		sys.exit()
	else:
		# Adds the information of the variable
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

def p_expression_log_point2(p):
	'''expression_log_point2 : '''

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

def p_expression_point2(p):
	'''expression_point2 : '''

def p_exp(p):
    '''exp : term exp_point
           | term exp_point PLUS exp_point2 exp
           | term exp_point MINUS exp_point2 exp '''

def p_exp_point(p):
	'''exp_point : '''

def p_exp_point2(p):
	'''exp_point2 : '''

def p_term(p):
    '''term : factor term_point
            | factor term_point TIMES term_point2 term
            | factor term_point DIVIDES term_point2 term'''

def p_term_point(p):
	'''term_point : '''

def p_term_point2(p):
	'''term_point2 : '''

def p_factor(p):
    '''factor : LPAREN factor_point expression_log RPAREN factor_point2
              | var_const '''

def p_factor_point(p):
	'''factor_point : '''

def p_factor_point2(p):
	'''factor_point2 : '''

def p_var_const(p):
    '''var_const : ID var_const_point list_call
                 | CONST_INT var_const_point2
                 | CONST_FLOAT var_const_point3
                 | CONST_STRING var_const_point4
                 | boolean var_const_point5
                 | function'''

def p_var_const_point(p):
	'''var_const_point : '''

def p_var_const_point2(p):
	'''var_const_point2 : '''

def p_var_const_point3(p):
	'''var_const_point3 : '''

def p_var_const_point4(p):
	'''var_const_point4 : '''

def p_var_const_point5(p):
	'''var_const_point5 : '''

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = p[1]

### RETURN

def p_return(p):
	'''return : RETURN expression_log SEMICOLON return_point'''
	quadruple = Quadruple(my_code.quadruple_number, 'RETURN', None, None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_return_point(p):
	'''return_point : '''

### FUNCTIONS

def p_functions(p):
    '''functions : FUNC type_func ID LPAREN params RPAREN functions_point block functions_point2 functions
                 | empty'''
    quadruple = Quadruple(my_code.quadruple_number, 'ENDFUNC', None, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

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

def p_functions_point(p):
	'''functions_point : '''

def p_functions_point2(p):
	'''functions_point2 : '''

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
    quadruple = Quadruple(my_code.quadruple_number, 'ASSIGN', None, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

def p_assignment_point(p):
	'''assignment_point : '''

def p_assignment_point2(p):
	'''assignment_point2 : '''

def p_assignment_point3(p):
	'''assignment_point3 : '''

def p_assignment_point4(p):
	'''assignment_point4 : '''



### LIST CALL

def p_list_call(p):
    '''list_call : LBRACKET list_point list_point2 exp list_point3 list_point4 RBRACKET
            	 | empty'''

def p_list_point(p):
	'''list_point : '''
    variable_name = p[-3]
    my_code.operand_list.pop()

    # Checks if the variable exists in the local scope
    variable = my_code.function_directory.get_function_variable(
        my_code.current_scope, variable_name)

    if variable is None:
        # Checks if the variable exists in the global scope
        variable = my_code.function_directory.get_function_variable(
            my_code.global_scope, variable_name)
        if variable is None:
            print("The variable " + variable_name + " has not been declared")
            sys.exit()
        else:
            if 'upper_limit' in variable:
                # Appends the dimensioned variable to a stack, makes nesting
                # vectors calls possible
                my_code.list_variable_list.append(variable)
            else:
                print("The variable " + variable_name + " is not an array")
                sys.exit()
    else:
        if 'upper_limit' in variable:
            # Appends the dimensioned variable to a stack, makes nesting
            # vectors calls possible
            my_code.list_variable_list.append(variable)
        else:
            print("The variable " + variable_name + " is not an array")
            sys.exit()

def p_list_point2(p):
	'''list_point2 : '''
	my_code.operator_list.append('()')

def p_list_point3(p):
	'''list_point3 : '''
    index_address = my_code.operand_list.pop()
    index_type = my_code.type_stack.pop()

    # Returns the last dimensioned variable called
    dimensioned_variable = my_code.list_variable_list.pop()

    # Verifies the type of the index
    if index_type != 'int':
        print("Array indexes should be of type int")
        sys.exit()
    else:
        # Verifies the boundaries
        quadruple = Quadruple(my_code.quadruple_number, 'VERF_INDEX',
            index_address, dimensioned_variable['lower_limit'], dimensioned_variable['upper_limit'])
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1

        # The base address of the dimensioned variable must be stored in new
        # address, this makes possible the adding of the base address number and
        # not its content
        base_address_proxy = my_code.memory.request_global_address('int',
            dimensioned_variable['memory_adress'])
        index_address_result = my_code.memory.request_global_address('int')

        # Adds the base address number with the result of the index
        quadruple = Quadruple(my_code.quadruple_number, '+', base_address_proxy,
            index_address, index_address_result)
        my_code.quadruple_list.append(quadruple)
        my_code.quadruple_number += 1

        # Stores the index address result int a dictionary to difference it
        # from a regular address
        result_proxy = {'index_address' : index_address_result}
        my_code.operand_list.append(result_proxy)
        my_code.type_stack.append(dimensioned_variable['type'])

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

def p_else(p):
	'''else : ELSE else_point block
	        | empty'''
	quadruple = Quadruple(my_code.quadruple_number, 'GOTO', None, None, None)

def p_else_point(p):
    '''else_point : '''

### WRITE

def p_write(p):
    '''write : PRINT LPAREN expression_log write_point RPAREN SEMICOLON'''
    quadruple = Quadruple(my_code.quadruple_number, 'PRINT', None, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

def p_write_point(p):
    '''write_point : '''

### LOOP

def p_loop(p):
    '''loop : WHILE loop_point LPAREN expression_log RPAREN loop_point2 block loop_point3'''
    quadruple = Quadruple(my_code.quadruple_number, 'GOTO', None, None, None)
    my_code.quadruple_list.append(quadruple)
    my_code.quadruple_number += 1

def p_loop_point(p):
    '''loop_point : '''

def p_loop_point2(p):
    '''loop_point2 : '''

def p_loop_point3(p):
    '''loop_point3 : '''

### METHOD

def p_method(p):
	'''method : ID LPAREN method_point method_point2 args RPAREN method_point3 method_point4 method_point5 SEMICOLON'''
	quadruple = Quadruple(my_code.quadruple_number, 'GOSUB', None, None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_method_point(p):
    '''method_point : '''

def p_method_point2(p):
    '''method_point2 : '''

def p_method_point3(p):
    '''method_point3 : '''

def p_method_point4(p):
    '''method_point4 : '''

def p_method_point5(p):
    '''method_point5 : '''

### FUNCTION

def p_function(p):
	'''function : ID LPAREN function_point function_point2 args RPAREN function_point3 function_point4 function_point5 '''
	quadruple = Quadruple(my_code.quadruple_number, 'GOSUB', None, None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_function_point(p):
    '''function_point : '''

def p_function_point2(p):
    '''function_point2 : '''

def p_function_point3(p):
    '''function_point3 : '''

def p_function_point4(p):
    '''function_point4 : '''

def p_function_point5(p):
    '''function_point5 : '''


### ARGUMENTS

def p_args(p):
	'''args : expression_log args_point args_aux
			| empty'''
	quadruple = Quadruple(my_code.quadruple_number, 'PARAMETER', None, None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_args_aux(p):
	'''args_aux : COMMA expression_log args_point args_aux
                | empty'''
	quadruple = Quadruple(my_code.quadruple_number, 'PARAMETER', None, None, None)
	my_code.quadruple_list.append(quadruple)
	my_code.quadruple_number += 1

def p_args_point(p):
    '''args_point : '''

### VAR STRING

def p_string_var(p):
    '''string_var : ID
                  | CONST_STRING'''

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




# Build the parser
parser = yacc.yacc()
with open("archivo_entrada.txt") as file_object:
    code = file_object.read()
    parser.parse(code)

my_code.print_quadruples()
