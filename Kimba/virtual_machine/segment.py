
class Segment():
    def __init__(self, segment_name, initial_address, last_address):
        """Class constructor"""
        self.name = segment_name
        self.initial_address = initial_address
        self.last_address = last_address
        self.current_address = initial_address
        self.segment = {}

    def is_available(self, num_of_addresses=1):
        if self.available_spaces() >= num_of_addresses:
            return True
        else:
            return False

    def available_spaces(self):
        return self.last_address - self.current_address

    def set_address_list(self, num_of_addresses, value):
        if self.is_available(num_of_addresses):
            base = self.current_address
            for i in range(num_of_addresses):
                self.segment[self.current_address] = value
                self.current_address += 1
            return base
        else:
            print("Error. Insufficient space on the segment")

    def set_address(self, value):
        if self.is_available():
            address = self.current_address
            self.segment[address] = value
            self.current_address += 1
            return address
        else:
            print("Error. Insufficient space on the segment")


    def get_value(self, address):
        if self.address_in_segment(address):
            return self.segment[address]
        else:
            print ("Error. Invalid address")
            return None

    def address_in_segment(self, address):
        if address in self.segment:
            return True
        else:
            return False

    def value_in_segment(self, value):
        for segment_address, segment_value in self.segment.items():
            if segment_value == value:
                return segment_address
        return None


    def set_value(self, value, address=None):
        if address is None:
            address = self.current_address
        if self.address_in_segment(address):
            self.segment[address] = value
        else:
            print("Error. Address not defined")

    def reset_segment(self):
        self.segment.clear()
        self.current_address = self.initial_address

    def print_segment(self):
        print(self.segment.items())


if __name__ == '__main__':
        segmento = Segment('prueba', 8000, 8999)
        segmento.set_address_list(5, '2002')
        segmento.set_value('value', 8100)
        #segmento.print_segment()
        resultado = segmento.value_in_segment('z')
        #print(segmento.is_available(594))
