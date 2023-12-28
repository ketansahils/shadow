import pandas as pd


if __name__ == '__main__':
    d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    df = pd.DataFrame(data=d, index=[0, 1, 2, 3])

    print(df)
