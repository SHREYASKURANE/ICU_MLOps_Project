import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "ICU.csv")

TRAIN_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "train_processed.csv")

TEST_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "test_processed.csv")

# Create directories if they don't exist
os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")

SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

MLFLOW_EXPERIMENT = "ICU_Patient_Deterioration"