from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

matchingIndices = []

for i in range(len(values)):
    if values[i] >= x:
        matchingIndices.append(i)

print(f"Sorted Values: {values}")
print(f"Threshold (x): {x}")

if len(matchingIndices) > 0:
    print(f"First matching index: {matchingIndices[0]}")
else:
    print("No values found greater than or equal to x.")