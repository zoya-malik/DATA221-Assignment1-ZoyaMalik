# DATA 221 - Assignment 1
# Question 6: Distribution Analysis

def calculateDistribution(numbers):
    # get sorted unique values using set
    uniqueValues = sorted(list(set(numbers)))
    # initialize dictionary for distribution
    distributionDict = {}
    # calculate total count of elements
    totalCount = len(numbers)

    # iterate through unique values
    for value in uniqueValues:
        count = 0
        # inner loop to count values less than or equal to current
        for num in numbers:
            if num <= value:
                count += 1
        # calculate percentage and update dictionary
        percentage = (count / totalCount) * 100
        distributionDict[value] = percentage

    return distributionDict


if __name__ == "__main__":
    # test list from assignment
    testNumbers = [3, 1, 2, 3, 4, 2]
    result = calculateDistribution(testNumbers)
    print("Input List:", testNumbers)
    print("Distribution Dictionary:")
    print("{")
    for key in result:
        print(f"  {key}: {result[key]}%,")
    print("}")