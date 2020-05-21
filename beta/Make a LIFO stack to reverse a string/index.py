# Beta - Make a LIFO stack to reverse a string

""" In this kata you have to implement a basic stack(LIFO) data structure. 
You have to implement the following methods:

__str__
      return a string "Stack of size: stack_size"  
      where stack_size is the current size of the stack

isEmpty
      return true if its empty and false otherwise

push
      add an element

pop
      remove the top element and return it

top
   return the top element without removing it or None if empty

You should then implement the reverse_str method that takes as input a string and a stack object 
and uses the stack to reverse the string. """


class CWStack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def top(self):
        return self.stack[-1] if self.size else None

    def pop(self):
        item = self.stack[-1]
        self.stack = self.stack[:-1]
        self.size -= 1
        return item

    def __str__(self):
        return 'Stack of size: ' + str(self.size)


def reverse_str(s, stack):
    res = []
    for x in s:
        stack.push(x)
    while not stack.isEmpty():
        res.append(stack.pop())
    return ''.join(res)


s = CWStack()

q = s.isEmpty(), True
q
s.push(10)
s
q = s.top(), 10
q
q = s.pop(), 10
q
q = s.__str__(), "Stack of size: 0"
q
q = reverse_str('hello', CWStack()), 'olleh'
q
