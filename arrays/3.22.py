import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]


arr = [10, 20, 30, 40, 50]

print("Random elements:")
for i in range(5):
    print(rand_elem(arr))