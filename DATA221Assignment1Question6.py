
def calculateDistribution(numbers):
    uniqueValues = sorted(list(set(numbers)))
    distributionDict = {}
    totalCount = len(numbers)

    for value in uniqueValues:
        count = 0
        for num in numbers:
            if num <= value:
                count += 1

        percentage = (count / totalCount) * 100
        distributionDict[value] = percentage

    return distributionDict


if __name__ == "__main__":
    testNumbers = [3, 1, 2, 3, 4, 2]
    result = calculateDistribution(testNumbers)
    print("Input List:", testNumbers)
    print("Distribution Dictionary:")
    print("{")
    for key in result:
        print(f"  {key}: {result[key]}%,")
    print("}")