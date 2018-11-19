import json

from assets.var_table import VarTable

class FunctionDirectory():

    """Constructor"""
    def __init__(self):
        self.func_list = {}

    """ Adds a function to the list """
    def add_function(self, func_name, func_type, parameter_list = [],
     parameter_addresses = []):
        self.func_list[func_name] = {
            'name' : func_name,
            'return_type' : func_type,
            'quadruple_number' : -1,
            'return_address' : -1,
            'parameters' :
            {
                'types' : parameter_list,
                'addresses' : parameter_addresses,
            },
            'variables' : VarTable(),
            'local_variables_counter' : {
                'int' : 0,
                'float' : 0,
                'string' : 0,
                'boolean' : 0
            },
            'temporal_variables_counter' : {
                'int' : 0,
                'float' : 0,
                'string' : 0,
                'boolean' : 0
            }
        }

    """ Check if a function exists in the list """
    def search_function(self, func_name):
        return func_name in self.func_list.keys()

    """ Get a function contained in the list """
    def get_function(self, func_name):
        if self.search_function(func_name):
            return self.func_list[func_name]
        else:
            print("The function does not exist")
            return None

    def get_function_type(self, function_name):
        """Looks for the type of the function"""""
        function = self.get_function(function_name)
        if function is not None:
            function_type = function['return_type']
            return function_type
        else:
            print("This function doesn't exists")

    """ Adds a paramter to a function """
    def add_parameter_to_function(self, func_name, type_list, address_list):
        function = self.get_function(func_name)
        if function is not None:
            function['parameters']['types'] = type_list
            function['parameters']['address'] = address_list
        else:
            print("The function does not exist")

    def get_function_quadruple_number(self, function_name,):
        """Retrieves the quadruple number of a function"""
        function = self.get_function(function_name)
        if function is not None:
            return function['quadruple_number']
        else:
            print("The function you are trying to retrieve its quadruple doesn't exists")


    def set_function_quadruple_number(self, function_name, quadruple_number):
        """Establish where the procedure starts"""
        function = self.get_function(function_name)
        if function is not None:
            function['quadruple_number'] = quadruple_number
        else:
            print("The function you are trying to set the quadruple doesn't exists")

    def set_function_address(self, function_name, address_number):
        """Sets the address return of the function"""
        function = self.get_function(function_name)
        if function is not None:
            function['return_address'] = address_number
        else:
            print("The function you are trying to add the adress doesn't exists")


    def check_existing_variable(self, function_name, variable_name):
        """Checks if a variable already exists in the function scope"""
        function = self.get_function(function_name)
        if function is not None:
            return function['variables'].search_var(variable_name)
        else:
            print("The variable " + variable_name + " has been already declared")



    def add_variable_to_function(self, function_name, variable_type,
            variable_name, variable_address=0):
        """Adds a variable to its function variable table"""
        function = self.get_function(function_name)
        if function is not None:
            if function['variables'].search_var(variable_name):
                print("This function already has a variable with that name")
            else:
                # Adds the variable to the variable table and increments the
                # number of local variables the function will use
                function['variables'].add_var(variable_type, variable_name, variable_address)
                function['local_variables_counter'][variable_type] += 1
        else:
            print("The function you are trying to add the variable doesnt exists")


    def add_list_variable_to_function(self, function_name, variable):
        """Adds a dimensioned variable to its function variable table"""
        function = self.get_function(function_name)
        if function is not None:
            if function['variables'].search_var(variable['name']):
                print("This function already has a variable with that name")
            else:
                # Adds the variable to the variable table and increments the
                # number of local variables the function will use
                function['variables'].add_list_var(variable)
                for i in range(variable['upper_limit']):
                    function['local_variables_counter'][variable['type']] += 1
        else:
            print("The function you are trying to add the variable doesnt exists")

    def get_function_variable(self, function_name, variable_name):
        """Looks for a variable in the function"""""
        function = self.get_function(function_name)
        if function is not None:
            variable = function['variables'].get_var(variable_name)
            if variable is not None:
                return variable
            else:
                return None
        else:
            print("The function you are trying to find when looking for the" + "variable doesn't exists")

    def get_function_parameters(self, function_name):
        """Returns the parameters of the function if exists"""
        function = self.get_function(function_name)
        if function is not None:
            return function['parameters']
        else:
            print("The function you are trying to retrieve its parameters" +
                "doesnt exists")

    def add_temporal_to_function(self, function_name, temporal_type):
        """Increments the number of temporals the function has"""
        function = self.get_function(function_name)
        if function is not None:
            function['temporal_variables_counter'][temporal_type] += 1
        else:
            print("The function you are trying to add the temporal doesnt exists")


    def print_directory(self):
        for p in self.func_list:
            print (p)


if __name__ == '__main__':
    params = ['par1', 'par2']
    directorio = FunctionDirectory()
    directorio.add_function('patito', 'int', ['par1', 'par2'])
    directorio.print_directory()
