# DATA 221 - Assignment 1
# Question 2: Nested Dictionary from Strings

def analyzeStringList(stringList):
    # initialize empty dictionary for results
    resultsDictionary = {}

    # iterate through each string in the list
    for currentString in stringList:
        # calculate the length of the string
        stringLength = len(currentString)
        # determine parity using the modulus operator
        if stringLength % 2 == 0:
            parityStatus = "even"
        else:
            parityStatus = "odd"

        # create inner dictionary with string metrics
        stringMetrics = {
            "length": stringLength,
            "parity": parityStatus
        }
        # assign inner dictionary to the key
        resultsDictionary[currentString] = stringMetrics

    return resultsDictionary

# test
if __name__ == "__main__":
    testInput = ["data", "science"]
    finalResult = analyzeStringList(testInput)
    print("{")
    for key in finalResult:
        print(f'    "{key}": {finalResult[key]},')
    print("}")