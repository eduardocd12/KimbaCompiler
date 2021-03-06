from virtual_machine.segment import Segment

class Memory():
    def __init__(self, memory_name, initial_address, num_of_addresses):
        """Class constructor"""
        self.name = memory_name
        self.size = int(num_of_addresses / 4)
        self.initial_address = initial_address
        self.last_address= initial_address + num_of_addresses - 1

        self.int_initial_address = initial_address
        self.int_last_address = initial_address + self.size - 1
        self.float_initial_address = self.int_last_address + 1
        self.float_last_address = self.float_initial_address + self.size - 1
        self.string_initial_address = self.float_last_address + 1
        self.string_last_address = self.string_initial_address + self.size - 1
        self.boolean_initial_address = self.string_last_address + 1
        self.boolean_last_address = self.boolean_initial_address + self.size - 1

        self.int_segment = Segment('Integer', self.int_initial_address,
            self.int_last_address)
        self.float_segment = Segment('Float', self.float_initial_address,
            self.float_last_address)
        self.string_segment = Segment('String', self.string_initial_address,
            self.string_last_address)
        self.boolean_segment = Segment('Boolean', self.boolean_initial_address,
            self.boolean_last_address)

    def get_address(self, segment_type, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.set_address(value)
        elif segment_type == 'float':
            if value is None:
                value = 0.0
            return self.float_segment.set_address(value)
        elif segment_type == 'string':
            if value is None:
                value = ""
            return self.string_segment.set_address(value)
        elif segment_type == 'boolean':
            if value is None:
                value = False
            return self.boolean_segment.set_address(value)

    def get_type(self, address):
        if (address >= self.int_initial_address and address <=
            self.int_last_address):
            return 'int'
        elif (address >= self.float_initial_address and address <=
            self.float_last_address):
            return 'float'
        elif (address >= self.string_initial_address and address <=
            self.string_last_address):
            return 'string'
        elif (address >= self.boolean_initial_address and address <=
            self.boolean_last_address):
            return 'boolean'
        else:
            print ("Error. Invalid address")

    def get_value(self, address):
        segment_type = self.get_type(address)
        if segment_type == 'int':
            return self.int_segment.get_value(address)
        elif segment_type == 'float':
            return self.float_segment.get_value(address)
        elif segment_type == 'string':
            return self.string_segment.get_value(address)
        elif segment_type == 'boolean':
            return self.boolean_segment.get_value(address)

    def get_address_list(self, segment_type, num_of_addresses, value=None):
        if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.set_address_list(num_of_addresses, value)
        elif segment_type == 'float':
            if value is None:
                value = 0.0
            return self.float_segment.set_address_list(num_of_addresses, value)
        elif segment_type == 'string':
            if value is None:
                value = ""
            return self.string_segment.set_address_list(num_of_addresses, value)
        elif segment_type == 'boolean':
            if value is None:
                value = False
            return self.boolean_segment.set_address_list(num_of_addresses, value)

    def in_segment(self, segment_type, value):
        if segment_type == 'int':
            return self.int_segment.value_in_segment(value)
        elif segment_type == 'float':
            return self.float_segment.value_in_segment(value)
        elif segment_type == 'string':
            return self.string_segment.value_in_segment(value)
        elif segment_type == 'boolean':
            return self.boolean_segment.value_in_segment(value)
            
    def set_value(self, address, value):
        segment_type = self.get_type(address)
        if segment_type == 'int':
            self.int_segment.set_value(value, address)
        elif segment_type == 'float':
            return self.float_segment.set_value(value, address)
        elif segment_type == 'string':
            return self.string_segment.set_value(value, address)
        elif segment_type == 'boolean':
            return self.boolean_segment.set_value(address, value)

    def reset_memory_segments(self):
        self.int_segment.reset_segment()
        self.float_segment.reset_segment()
        self.string_segment.reset_segment()
        self.boolean_segment.reset_segment()

    def print_segment(self, segment_type):
        if segment_type == 'int':
            self.int_segment.print_segment()
        elif segment_type == 'float':
            self.float_segment.print_segment()
        elif segment_type == 'string':
            self.string_segment.print_segment()
        elif segment_type == 'boolean':
            self.boolean_segment.print_segment()
        else:
            print("Error. Ivalid type")

if __name__ == '__main__':
    segmento = Memory('patito', 5000, 4000)
    add = segmento.get_address('int')
    #print(add)
    #segmento.int_segment.set_address_list(5, 'hola')
    segmento.get_address_list('int', 200, 'prueba')
    add = segmento.get_address_list('boolean', 500, 'hello')
    #print(add)
    #print(segmento.get_value(8400))
    #print(segmento.get_type(8100))
    segmento.set_value(8100, 'holanda')
    segmento.reset_memory_segments()
    segmento.print_segment('int')
    #print(segmento.get_address('boolean', 8100))
