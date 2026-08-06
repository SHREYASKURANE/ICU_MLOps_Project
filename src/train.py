import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from config import (
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    MODEL_PATH,
    MLFLOW_EXPERIMENT,
)

# Load Data
train = pd.read_csv(TRAIN_DATA_PATH)
test = pd.read_csv(TEST_DATA_PATH)

X_train = train.drop("Survive", axis=1)
y_train = train["Survive"]

X_test = test.drop("Survive", axis=1)
y_test = test["Survive"]

# MLflow Experiment
mlflow.set_experiment(MLFLOW_EXPERIMENT)

with mlflow.start_run():

    model = LogisticRegression(
        random_state=42,
        max_iter=500
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    # Log Parameters
    mlflow.log_param("Model", "LogisticRegression")
    mlflow.log_param("Random State", 42)
    mlflow.log_param("Max Iterations", 500)

    # Log Metrics
    mlflow.log_metric("Accuracy", accuracy)
    mlflow.log_metric("Precision", precision)
    mlflow.log_metric("Recall", recall)
    mlflow.log_metric("F1 Score", f1)

    # Save Confusion Matrix
    cm = confusion_matrix(y_test, predictions)

    with open("confusion_matrix.txt", "w") as f:
        f.write(str(cm))

    mlflow.log_artifact("confusion_matrix.txt")

    # Save Model
    mlflow.sklearn.log_model(model, "LogisticRegression")

    joblib.dump(model, MODEL_PATH)

    print("=" * 50)
    print("Model Trained Successfully")
    print("=" * 50)
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")