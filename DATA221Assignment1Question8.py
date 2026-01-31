# DATA 221 - Assignment 1
# Question 8: Pandas DataFrame with Computed Column

import pandas as pd

def createAndModifyDataFrame():
    # define dictionary with input data
    data = {
        "A": [1, 2, 2, 1],
        "B": [3.1, 4.2, 1.5, 6.3],
        "C": [800, 150, 400, 210]
    }
    # create dataframe using pandas
    df = pd.DataFrame(data)
    # perform vectorized multiplication for new column
    df['D'] = df['A'] * df['B']

    return df


if __name__ == "__main__":
    finalDF = createAndModifyDataFrame()
    print("Final DataFrame Output:")
    print(finalDF)