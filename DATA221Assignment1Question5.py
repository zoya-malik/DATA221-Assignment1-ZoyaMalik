# DATA 221 - Assignment 1
# Question 5: Circle Area Comparison with Validation

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # validate that radius 1 is a positive integer
    if not (isinstance(radiusOfCircle1, int) and radiusOfCircle1 > 0):
        return "Invalid input: radiusOfCircle1 must be a positive integer."
    # validate that radius 2 is a positive integer
    if not (isinstance(radiusOfCircle2, int) and radiusOfCircle2 > 0):
        return "Invalid input: radiusOfCircle2 must be a positive integer."

    # compute area for both circles using math.pi
    area1 = math.pi * (radiusOfCircle1 ** 2)
    area2 = math.pi * (radiusOfCircle2 ** 2)

    # compare areas to determine larger and smaller
    if area1 > area2:
        largerArea = area1
        smallerArea = area2
    else:
        largerArea = area2
        smallerArea = area1
    # compute coverage percentage
    coveragePercentage = (smallerArea / largerArea) * 100

    return coveragePercentage


if __name__ == "__main__":
    # Test Case 1
    r1 = 10
    r2 = 5
    result = circleAreaCoverage(r1, r2)
    print(f"Radius 1: {r1}, Radius 2: {r2}")
    print(f"Coverage: {result}%")

    # Test Case 2
    print(f"Test Invalid: {circleAreaCoverage(-5, 10)}")

    # Test Case 3
    print(f"Test Decimal: {circleAreaCoverage(5.5, 10)}")