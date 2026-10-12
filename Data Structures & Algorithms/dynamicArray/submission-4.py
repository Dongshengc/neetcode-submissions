class DynamicArray:
    
    def __init__(self, capacity: int):

        self.list = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:

        return self.list[i]

    def set(self, i: int, n: int) -> None:

        self.list[i] = n

    def pushback(self, n: int) -> None:

        if self.length == self.capacity:
            self.resize()
        self.list[self.length] = n
        self.length += 1
        
    def popback(self) -> int:
        
        self.length -= 1
        temp = self.list[self.length]
        self.list[self.length] = None

        return temp
 
    def resize(self) -> None:

        new_list = [None] * self.getCapacity()
        self.capacity *= 2

        self.list.extend(new_list)

    def getSize(self) -> int:

        return self.length        
    
    def getCapacity(self) -> int:

        return len(self.list)