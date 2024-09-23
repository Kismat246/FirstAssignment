class DynamicArrayList:

    def __init__(self, initial_size=2):
        self.eowl = [None, None]
        self.size = 0
        self.size_limit = initial_size

    def __str__(self):
        return f"{self.eowl} {self.size} {self.size_limit}"
    
    def add_word(self, word):
        if(self.size == self.size_limit):
            self.resize()

        self.eowl[self.size] = word
        self.size += 1 

    
    def resize(self):
        self.increase_size_by_10()
        new_eowl = [None] * self.size_limit

        #copying the previous array items to new array
        for idx in range(self.size):
            new_eowl[idx] = self.eowl[idx]
        
        #replacing the previous array with new large array
        self.eowl = new_eowl

    def increase_size_by_10(self):
         # strategyA: Incremental: increase the size of eowl[] by 10
        self.size_limit += 10

    def increase_size_by_double(self):
        #Increase strategyB: Doubling: double the size of eowl[]
        self.size_limit *= 2
    

dynamic_array_list = DynamicArrayList()

words = ['yellow', 'red', "pink"]

for word in words:
    dynamic_array_list.add_word(word)

print(dynamic_array_list.eowl)