
import pandas as pd

def createAndModifyDataFrame():
    data = {
        "A": [1, 2, 2, 1],
        "B": [3.1, 4.2, 1.5, 6.3],
        "C": [800, 150, 400, 210]
    }

    df = pd.DataFrame(data)
    df['D'] = df['A'] * df['B']

    return df


if __name__ == "__main__":
    finalDF = createAndModifyDataFrame()
    print("Final DataFrame Output:")
    print(finalDF)