'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Implement the following operations of a stack using queues:
     • push(x): Push element x onto stack.
     • pop(): Removes the element on top of the stack.
     • top(): Get the top element.
     • empty(): Return whether the stack is empty.

Note: 
• You must use only standard operations of a queue, which means 
  only push to back, peek/pop from front, size, and is empty 
  operations are valid.
• Depending on your language, queue may not be supported natively.
• You may simulate a queue by using a list or deque (double-ended 
  queue), as long as you use only standard operations of a queue.
• You may assume that all operations are valid (e.g. no pop or top 
  operations will be called on an empty stack).

Examples:
//     stack = MyStack()
//     stack.push(3)
//     stack.push(7)
//     stack.top()        // returns 7
//     stack.pop()        // returns 7
//     stack.isEmpty()    // returns False
//     stack.top()        // returns 3
//     stack.pop()        // returns 3
//     stack.isEmpty()    // returns True

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
'''
class MyStack:
    # Write your code here.
    

    def __init__(self):
        from collections import deque
        self.q = deque()

    # Push element x onto stack.
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        
    # Removes the element on top of the stack and returns that element.
    def pop(self) -> int:
  
        return self.q.popleft()

    # Get the top element
    def top(self) -> int:
        return self.q[0]
  
    #Returns whether the stack is empty.
    def isEmpty(self) -> bool:
        return not self.q  

# Test Cases
stack1 = MyStack()
print(stack1.isEmpty(), 'expect True')
stack1.push(1)
print(stack1.top(), 'expect 1')
stack1.push(2)
print(stack1.top(), "expect 2")
print(stack1.pop(), "expect 2")
print(stack1.isEmpty(), 'expect False') 
print(stack1.pop(), 'expect 1')
print(stack1.isEmpty(), 'expect True')