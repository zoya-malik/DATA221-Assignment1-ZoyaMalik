# DATA 221 - Assignment 1
# Question 3: Safe Function Application

# define function to calculate power
def calculatePower(base, exponent):
    return base ** exponent

# define input list of number pairs
pairs = [[5, 2], [3, 1], [4, 3], [2, 0]]
# initialize list for valid results
validResults = []

# iterate and unpack base and exponent from pairs
for x, y in pairs:
    # check if exponent non-negative
    if y >= 0:
        result = calculatePower(x, y)
        validResults.append(result)

print(validResults)