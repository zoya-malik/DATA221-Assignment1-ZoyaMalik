# Question 2: Nested Dictionary from Strings
def analyzeStringList(stringList):
    resultsDictionary = {}

    for currentString in stringList:
        stringLength = len(currentString)
        if stringLength % 2 == 0:
            parityStatus = "even"
        else:
            parityStatus = "odd"

        stringMetrics = {
            "length": stringLength,
            "parity": parityStatus
        }
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