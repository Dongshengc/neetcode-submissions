class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []
        self.min_val = 2 ** 31
        

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if self.stack[-1] <= self.min_stack[-1]:
                self.min_stack.append(self.stack[-1])
            else:
                self.min_stack.append(self.min_stack[-1])

        # print("after push stack", self.stack)
        # print("after push min_stack", self.min_stack)

    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()

        

        # print("after pop stack", self.stack)
        # print("after pop min_stack", self.min_stack)
        
    def top(self) -> int:

        return self.stack[-1]
        
    def getMin(self) -> int:

        return self.min_stack[-1]
        
