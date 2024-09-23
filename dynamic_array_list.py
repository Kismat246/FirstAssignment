class DynamicArrayList:

    def __init__(self, initial_size=2):
        self.array = [None, None]
        self.size = 0
        self.size_limit = initial_size

    def __str__(self):
        return f"{self.array} {self.size} {self.size_limit}"
    
    def resize():
        print('resize')

dynamic_array_list = DynamicArrayList()
