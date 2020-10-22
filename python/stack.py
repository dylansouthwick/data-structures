class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.container = []

  def push(self,value):
    self.container.append(value)

  def pop(self):
    return self.container.pop()

  def size(self):
    return len(self.container)
  
  def __str__(self):
    return str(self.container)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack) # 123

print('popped last one', stack.pop()) #3
print(stack) #12
