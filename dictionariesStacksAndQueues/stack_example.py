import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""

stack = []

# i–vii: put numbers on the stack
stack.append(2)
stack.append(3)
stack.append(7)
stack.append(4)
stack.append(1)
stack.append(9)
stack.append(8)

print("Stack after pushes:", stack)

# viii: sum the last two numbers and print result
last = stack.pop()
second_last = stack.pop()
sum_last_two = last + second_last
print("Sum of last two numbers:", sum_last_two)

# ix: calculate the sum of remaining stack elements using while loop
total_sum = 0
while stack:
    total_sum += stack.pop()

print("Sum of remaining stack elements:", total_sum)
