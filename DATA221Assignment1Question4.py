# DATA 221 - Assignment 1
# Question 4: Sorted Search with Conditions

from random import random
# generate a list of 20 random values
values = [random() for i in range(20)]
# random threshold value
x = random()
# sort list in ascending order
values.sort()
# initialize list to store matching indices
matchingIndices = []
# iterate through list indices using range
for i in range(len(values)):
    # check if value meets the threshold condition
    if values[i] >= x:
        matchingIndices.append(i)

print(f"Sorted Values: {values}")
print(f"Threshold (x): {x}")

# check if matches exist and print the first index
if len(matchingIndices) > 0:
    print(f"First matching index: {matchingIndices[0]}")
else:
    print("No values found greater than or equal to x.")