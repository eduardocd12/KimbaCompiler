import json

from var_table import VarTable

class FunctionDirectory():

    """Constructor"""
    def __init__(self):
        self.func_list = {}

    """ Adds a function to the list """
    def add_function(self, func_name, func_type, parameter_list = [],
     parameter_adresses = []):
        self.func_list[func_name] = {
            'name' : func_name,
            'return_type' : func_type,
            'quadruple_number' : -1,
            'return_address' : -1,
            'parameters' :
            {
                'types' : parameter_list,
                'addresses' : parameter_adresses,
            },
            'variables' : VarTable(),
            'local_variables_counter' : {
                'int' : 0,
                'float' : 0,
                'string' : 0,
                'bool' : 0
            },
            'temporal_variables_counter' : {
                'int' : 0,
                'float' : 0,
                'string' : 0,
                'bool' : 0
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


    """ Adds a paramter to a function """
    def add_parameter(self, func_name, type_list, address_list):
        function = self.get_function(func_name)
        if function is not None:
            function['parameters']['types'] = type_list
            function['parameters']['address'] = address_list
        else:
            print("The function does not exist")

    def print_directory(self):
        for p in self.func_list:
            print (p)
        

if __name__ == '__main__':
    params = ['par1', 'par2']
    directorio = FunctionDirectory()
    directorio.add_function('patito', 'int', ['par1', 'par2'])
    directorio.print_directory()