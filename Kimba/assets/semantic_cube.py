class SemanticCube():

    def __init__(self):
        self.cube = {
            "int" : {
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "*" : "int",
                    "/" : "int",
                    "<" : "boolean",
                    "<=" : "boolean",
                    ">" : "boolean",
                    ">=" : "boolean",
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "int",
                    "and" : "error",
                    "or" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "<" : "boolean",
                    "<=" : "boolean",
                    ">" : "boolean",
                    ">=" : "boolean",
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "boolean" : {
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
                    "<" : "boolean",
                    "<=" : "boolean",
                    ">" : "boolean",
                    ">=" : "boolean",
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "<" : "boolean",
                    "<=" : "boolean",
                    ">" : "boolean",
                    ">=" : "boolean",
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "float",
                    "and" : "error",
                    "or" : "error"
                },
                "boolean" : {
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
            "boolean" : {
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
                "boolean" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "<" : "error",
                    "<=" : "error",
                    ">" : "error",
                    ">=" : "error",
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "boolean",
                    "and" : "boolean",
                    "or" : "boolean"
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
                "boolean": {
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
                    "==" : "boolean",
                    "!=" : "boolean",
                    "=" : "string",
                    "and" : "error",
                    "or" : "error"
                }
            }
        }

    def get_semantic_type(self, left_type, right_type, operator):
        return self.cube[left_type][right_type][operator]
