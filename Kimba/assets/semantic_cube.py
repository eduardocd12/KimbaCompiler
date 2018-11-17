class SemanticCube():

    def __init__(self):
        self.cube = {
            "int" : {
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "*" : "int",
                    "/" : "int",
                    "<" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    ">=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "int",
                    "and" : "error",
                    "or" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "<" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    ">=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "string": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                }
            },
            "float" : {
                "int" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "<" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    ">=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "<" : "bool",
                    "<=" : "bool",
                    ">" : "bool",
                    ">=" : "bool",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "string": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                }
            },
            "bool" : {
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "bool",
                    "and" : "bool",
                    "or" : "bool"
                },
                "string": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                }
            },
            "string": {
                "int": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "float": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "bool": {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "error",
                    "!=" : "error",
                    "=" : "error",
                    "and" : "error",
                    "or" : "error"
                },
                "string": {
                    "+" : "string",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "bool",
                    "!=" : "bool",
                    "=" : "string",
                    "and" : "error",
                    "or" : "error"
                }
            }
        }

    def get_semantic_type(self, left_type, right_type, operator):
        return self.cube[left_type][right_type][operator]