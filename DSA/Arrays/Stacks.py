class StackClass:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
        return f"Append {val} to stack"
    def checkEmpty(self):
        return (len(self.stack)==0)
    def PopTopValue(self):
        if(self.checkEmpty()):
            return "Stack is kinda... empty?"
        else:
            self.stack.pop()
            return "Popped the top value"
    def Peek(self):
            if(self.checkEmpty()):
                print("Stack is kinda... empty?")
            else:
                return f"Top value is {self.stack[-1]}" #-1 cause we using the built-in negative indexing method

stack1 = StackClass()
print(stack1.checkEmpty)
for x in range(10): 
    print(stack1.push(x))
print(stack1.Peek())
print(stack1.PopTopValue())
print(stack1.Peek())

