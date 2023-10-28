"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start):
        self.num = start 
        self.add = 0
        self.start = start

    def generate(self):
        sum = self.num + self.add
        self.add +=1
        return sum

    def reset(self):
        self.num = self.start
        self.add =0
        
        