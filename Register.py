from Content_Array import Content_Array
from Content_Array import Content_Array_16


class Register:
    def __init__(self, name, enableLowHigh):
        self.low = None
        self.name = name
        if enableLowHigh:
            self.content = Content_Array()
            # Allows access to individual 8-bits
        else:
            self.content = Content_Array_16()
            # Does not allow access to individual 8-bits

    def getLow(self):
        self.low = self.content.getLow()
