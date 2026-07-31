import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config import (
    RAW_DATA_PATH,
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    SCALER_PATH,
)

df = pd.read_csv(RAW_DATA_PATH)

df = df.drop(columns=["Unnamed: 0", "ID"])

X = df.drop("Survive", axis=1)

y = df["Survive"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

X_train = pd.DataFrame(X_train, columns=X.columns)

X_test = pd.DataFrame(X_test, columns=X.columns)

X_train["Survive"] = y_train.reset_index(drop=True)

X_test["Survive"] = y_test.reset_index(drop=True)

X_train.to_csv(TRAIN_DATA_PATH, index=False)

X_test.to_csv(TEST_DATA_PATH, index=False)

joblib.dump(scaler, SCALER_PATH)

print("Preprocessing Completed Successfully")