# Beta - Two Stacks Make A Queue

""" Stacks and queues. 
Staples of the computer science curriculum and remarkably useful data structures given their simplicity. 
They are sets, each with a special rule regarding how elements may be removed. 
In a stack, only the most recently added item may be removed. 
In a queue, it is the least recently added. 
Stacks are last in, first out (LIFO). 
Queues are first in, first out (FIFO).

But did you know that a queue can be implemented using two stacks?

This problem asks you to do just that. """


# class QueueFromStack:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#         self.size = 0
#         self.enqueue_mode = True

#     def enqueue(self, x):
#         while self.stack1:
#             self.stack2.append(self.stack1[-1])
#             self.stack1.pop()

#         self.stack1.append(x)

#         while self.stack2:
#             self.stack1.append(self.stack2[-1])
#             self.stack2.pop()

#         self.size += 1
#         self.enqueue_mode = True

#     def dequeue(self):
#         if self.stack1:
#             item = self.stack1[-1]
#             self.stack1.pop()
#             self.enqueue_mode = False
#             self.size -= 1
#             return item
#         else:
#             return 'Q is Empty'

#     def length(self):
#         return self.size


class QueueFromStack:
    def __init__(self):
        self.inbox = []
        self.outbox = []
        self.enqueue_mode = True

    def enqueue(self, x):
        if self.enqueue_mode is False:
            while len(self.outbox) > 0:
                self.inbox.append(self.outbox.pop())
        self.enqueue_mode = True
        self.inbox.append(x)

    def dequeue(self):
        if self.enqueue_mode is True:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        self.enqueue_mode = False
        return self.outbox.pop()

    def length(self):
        return len(self.inbox) + len(self.outbox)


q = QueueFromStack()

q.enqueue(1)
q.enqueue(2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(6)
q.enqueue(7)

p = q.dequeue(), 1
p
p = q.dequeue(), 2
p
p = q.length()
p
