
""""Key Data Structure that stores the list of variables of a 
           function, including the name and type of each variable. """
class VarTable():

    def __init__(self):
        self.var_list = {}

def add_var(self, var_type, var_name, var_adress = 0):
        self.var_list[var_name] = {
            'name' : var_name,
            'type' : var_type,
            'address' : var_address
        }

def search_var(self, var_name):
    return variable_name in self.variable_list.keys()


def get_var(self, var_name):
    if self.search_var(var_name):
        return self.var_list[var_name]
    else:
        return None

def __str__(self):
    return self.variable_list