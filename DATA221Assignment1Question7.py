# DATA 221 - Assignment 1
# Question 7: Time Conversion Function

def convertSecondsToTime(secondsSinceMidnight):
    # validate input is a non-negative integer
    if not (isinstance(secondsSinceMidnight, int) and secondsSinceMidnight >= 0):
        return "Invalid input: seconds must be a non-negative integer."

    # calculate hours using floor division
    rawHours = secondsSinceMidnight // 3600
    # use modulus to get 24-hour format
    hours24 = rawHours % 24
    # calculate remaining seconds using modulus
    secondsRemaining = secondsSinceMidnight % 3600
    # compute minutes and final seconds
    minutes = secondsRemaining // 60
    seconds = secondsRemaining % 60

    # determine am or pm suffix
    if hours24 >= 12:
        period = "PM"
    else:
        period = "AM"
    # convert 24-hour format to 12-hour display
    if hours24 == 0:
        displayHour = 12
    elif hours24 > 12:
        displayHour = hours24 - 12
    else:
        displayHour = hours24

    return f"{displayHour} {minutes} {seconds} {period}"

if __name__ == "__main__":
    # test with example value
    testSeconds = 19067
    print(f"Input: {testSeconds}")
    print(f"Output: {convertSecondsToTime(testSeconds)}")
    print(f"Midnight Test: {convertSecondsToTime(0)}")
    print(f"1 PM Test: {convertSecondsToTime(46800)}")
    print(f"Invalid Test: {convertSecondsToTime(-50)}")