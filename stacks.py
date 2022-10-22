# Martin Hoang 

'''
Stacks
The purpose of this program is to understand stack DS 

PSEUDOCODE: 
1. 

NOTES: 
- Stack implemented using a list DS. Use append and pop methods
- stacks are LIFO. Think of a stack of folded clothes 
- Implement stack collection module and deque class or make my own class 


'''
from collections import deque

# IMPLEMENTATION USING LIST 
stack1 = [] 
stack1.append(1)
stack1.append(5) 
stack1.append(10) 
print(stack1) 
stack1.pop()
print(stack1)  


# IMPLEMENTATION USING DEQUE CLASS 
stack2 = deque() 
stack2.appendleft(100) 
stack2.appendleft(50) 
stack2.appendleft(33) 
print(stack2) 
stack2.pop() 
print(stack2)


# IMPLEMENTATION MAKING CLASS 
class stack(): 
    def __init__(self): 
        self.stack = [] 

    def append(self, value): 
        self.stack.append(value)
    
    def remove(self): 
        # check that stack isn't empty 
        if len(self.stack) > 0: 
            self.stack.pop() 
        
    def peek(self): 
        size = len(self.stack) 
        if size > 0: 
            print(self.stack[size-1])
    
    def print_stack(self): 
        print(self.stack) 
    
stack3 = stack()
stack3.append(5) 
stack3.peek() 
stack3.append(4) 
stack3.append(1) 
stack3.print_stack() 



'''
QUESTIONS: 
-


LESSONS LEARNED: 
- A stack or queue can be implemented using deque class because elements can be added/removed from both ends 


CODE IMPROVEMENT: 
- 

'''