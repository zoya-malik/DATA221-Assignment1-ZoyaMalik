
def convertSecondsToTime(secondsSinceMidnight):
    if not (isinstance(secondsSinceMidnight, int) and secondsSinceMidnight >= 0):
        return "Invalid input: seconds must be a non-negative integer."

    rawHours = secondsSinceMidnight // 3600
    hours24 = rawHours % 24
    secondsRemaining = secondsSinceMidnight % 3600
    minutes = secondsRemaining // 60
    seconds = secondsRemaining % 60

    if hours24 >= 12:
        period = "PM"
    else:
        period = "AM"
    if hours24 == 0:
        displayHour = 12
    elif hours24 > 12:
        displayHour = hours24 - 12
    else:
        displayHour = hours24

    return f"{displayHour} {minutes} {seconds} {period}"

if __name__ == "__main__":

    testSeconds = 19067
    print(f"Input: {testSeconds}")
    print(f"Output: {convertSecondsToTime(testSeconds)}")
    print(f"Midnight Test: {convertSecondsToTime(0)}")
    print(f"1 PM Test: {convertSecondsToTime(46800)}")
    print(f"Invalid Test: {convertSecondsToTime(-50)}")