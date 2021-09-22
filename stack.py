from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    
def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()
    return rstr

if __name__ == '__main__':
    
    s=Stack()
    s.push(4)
    s.push(56)
    s.push(67)
    print(s.pop())
    print(s.peek())
    print(s.size())
    print(reverse_string("this is utsav"))
