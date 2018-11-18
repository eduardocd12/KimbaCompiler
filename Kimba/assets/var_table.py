
""""Key Data Structure that stores the list of variables of a
           function, including the name and type of each variable. """
class VarTable():

    def __init__(self):
        self.var_list = {}

    def add_var(self, var_type, var_name, var_address = 0):
            self.var_list[var_name] = {
                'name' : var_name,
                'type' : var_type,
                'memory_address' : var_address
            }

    def add_list_var(self, variable):
        """Adds a dimensioned variable to the list"""
        self.var_list[variable['name']] = variable

    def search_var(self, var_name):
        return var_name in self.var_list.keys()


    def get_var(self, var_name):
        if self.search_var(var_name):
            return self.var_list[var_name]
        else:
            return None

    def __str__(self):
        return self.var_list
