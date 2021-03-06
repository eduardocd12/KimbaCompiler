from virtual_machine.memory import Memory

class MemoryRequest():
    def __init__(self):
        self.global_memory = Memory('Global', 10000, 4000)
        self.local_memory = Memory('Local', 15000, 4000)
        self.constant_memory = Memory('Constant', 20000, 4000)
        self.temporal_memory = Memory('Temporal', 25000, 4000)

    def get_global_address(self, value_type, value=None,):
    	return self.global_memory.get_address(value_type, value)

    def get_local_address(self, value_type, value=None,):
    	return self.local_memory.get_address(value_type, value)

    def get_constant_address(self, value_type, value=None):
    	return self.constant_memory.get_address(value_type, value)

    def get_temporal_address(self, value_type, value=None):
    	return self.temporal_memory.get_address(value_type, value)

    def get_global_address_list(self, value_type, total_addresses, value=None):
        return self.global_memory.get_address_list(value_type,
            total_addresses, value)

    def get_local_address_list(self, value_type, total_addresses, value=None):
        return self.global_memory.get_address_list(value_type,
            total_addresses, value)

    def get_memory_type(self, address):
        if (address >= self.global_memory.initial_address and address <= self.global_memory.last_address):
            print("Entro global:" + str(address))
            return 'global'
        elif (address >= self.local_memory.initial_address and address <= self.local_memory.last_address):
            print("Entro local:"  + str(address))
            return 'local'
        elif (address >= self.temporal_memory.initial_address and address <= self.temporal_memory.last_address):
            print("Entro temporal:"  + str(address))
            return 'temporal'
        elif (address >= self.constant_memory.initial_address and address <= self.constant_memory.last_address):
            print("Entro constant:"  + str(address))
            return 'constant'
        else:
            print("Error. Invalid address")
            sys.exit()

    def get_value(self, address):
        memory_type = self.get_memory_type(address)
        if memory_type == 'global':
            return self.global_memory.get_value(address)
        elif memory_type == 'local':
            return self.local_memory.get_value(address)
        elif memory_type == 'temporal':
            return self.temporal_memory.get_value(address)
        elif memory_type == 'constant':
            return self.constant_memory.get_value(address)

    def set_value(self, address, value):
      type=self.get_memory_type(address)
      if type=='global':
        self.global_memory.set_value(address, value)
      elif type=='local':
        self.local_memory.set_value(address, value)
      elif type=='constant':
        self.constant_memory.set_value(address, value)
      elif type=='temporal':
        self.temporal_memory.set_value(address, value)
      else:
        print("Error. Invalid memory type")
        sys,exit()

    def restart_memory(self):
      self.local_memory.reset_memory_segments()
      self.temporal_memory.reset_memory_segments()

    def check_existing_constant_value(self, value_type, value):
        return self.constant_memory.in_segment(value_type, value)

    def print_memory(self, memory_type, segment_type):
      if memory_type == 'global':
        self.global_memory.print_segment(segment_type)
      elif memory_type == 'local':
        self.local_memory.print_segment(segment_type)
      elif memory_type == 'temporal':
        self.temporal_memory.print_segment(segment_type)
      elif memory_type == 'constant':
        self.constant_memory.print_segment(segment_type)
      else:
        print("Error. Invalid memory type")
        sys.exit()
