from .memory_segment import MemorySegment

class Memory():
    def __init__(self):
        """Class constructor"""
        self.global_memory = MemorySegment('Global', 10000, 4000)
        self.local_memory = MemorySegment('Local', 15000, 4000)
        self.constant_memory = MemorySegment('Constant', 20000, 4000)
        self.temporal_memory = MemorySegment('Temporal', 25000, 4000)

    def get_global_address(self, value):
    	return.self.global_memory.get_address(value_type, value)

    def get_local_address(self, value):
    	return.self.local_memory.get_address(value_type, value)

    def get_constant_address(self, value):
    	return.self.constant_memory.get_address(value_type, value)

	  def get_temporal_address(self, value):
    	return.self.temporal_memory.get_address(value_type, value)

    def get_global_address_list(self, value_type, num_of_address, value = None):
      if segment_type == 'int':
            if value is None:
                value = 0
            return self.int_segment.get_address_list(num_of_address_value, value)
      elif segment_type == 'float':
            if value is None:
                value = 0.0
            return self.float_segment.get_address_list(num_of_address_value, value)
      elif segment_type == 'string':
            if value is None:
                value = ""
            return self.string_segment.get_address_list(num_of_address_value, value)
      elif segment_type == 'bool':
            if value is None:
                value = False
            return self.bool_segment.get_address_list(num_of_address_value, value)


  	def get_memory_type(self, address):
  	if (address >= self.global_memory.initial_addres and address <= self.global_memory.last_address):
      return 'global'
    elif (address >= self.local_memory.initial_addres and address <= self.local_memory.last_address):
      return 'local'
    elif (address >= self.temporal_memory.initial_addres and address <= self.temporal_memory.last_address):
      return 'temporal'
    elif (address >= self.constant_memory.initial_addres and address <= self.constant_memory.last_address):
      return 'constant'
  	else:
      print("Error. Invalid address")

    def get_value(self, address):
      memory_type=self.get_memory_type(address)
      if memory_type=='global':
        return self.get_global_address(address)
      elif memory_type=='local':
        return self.get_local_address(address)
      elif memory_type=='constant':
        return self.get_constant_address(address)
      elif memory_type=='temporal':
        return self.get_temporal_address(address)
      else:
        print("Error. Invalid memory type")

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

    def restart_memory(self):
      self.local_memory.restart_memory()
      self.temporal_memory.restart_memory()


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