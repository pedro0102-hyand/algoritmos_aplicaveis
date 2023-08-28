import random
def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index  
    return -1  
array = [random.randint(1, 100) for _ in range(10)]
target = random.randint(1, 100)
print(f"Array: {array}")
print(f"Target: {target}")
result = linear_search(array, target)
if result != -1:
    print(f"O elemento {target} foi encontrado no índice {result}.")
else:
    print(f"O elemento {target} não foi encontrado no array.")

