class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)


top_item = stack.pop()
print("Popped:", top_item)
print("Stack after pop:", stack.items)

peeked_item = stack.peek()
print("Peeked:", peeked_item)
print("Stack size:", stack.size())

# Queue >>

# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             print("Error: Queue is empty")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             print("Error: Queue is empty")

#     def size(self):
#         return len(self.items)

# # Example usage:
# queue = Queue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print("Queue:", queue.items)

# front_item = queue.dequeue()
# print("Dequeued:", front_item)
# print("Queue after dequeue:", queue.items)

# peeked_item = queue.peek()
# print("Peeked:", peeked_item)
# print("Queue size:", queue.size())