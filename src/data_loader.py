import pandas as pd
from config import RAW_DATA_PATH


def load_data():
    df = pd.read_csv(RAW_DATA_PATH)
    return df


if __name__ == "__main__":
    df = load_data()

    print(df.head())