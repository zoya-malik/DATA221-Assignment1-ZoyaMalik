def calculatePower(base, exponent):
    return base ** exponent

pairs = [[5, 2], [3, 1], [4, 3], [2, 0]]
validResults = []

for x, y in pairs:
    if y >= 0:
        result = calculatePower(x, y)
        validResults.append(result)

print(validResults)