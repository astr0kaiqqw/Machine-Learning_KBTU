from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib
import mlflow
import mlflow.sklearn


mlflow.set_experiment("iris_classification_expirement")

with mlflow.start_run():
    iris = load_iris()
    X = iris.data
    y = iris.target 

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = 42
    )

    max_iter = 200

    model = LogisticRegression(max_iter = max_iter)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average = "weighted")

    joblib.dump(model, "model.joblib")

    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_param("max_iter", max_iter)
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)

    mlflow.log_artifact("model.joblib")

    mlflow.sklearn.log_model(
        sk_model = model,
        artifact_path = "iris_model",
        registered_model_name = "Iris_Logistic_Regression_Model"
    )

    print("Model trained and saved as model.joblib")
    print(f"Accuracy: {accuracy}")
    print(f"F1-score: {f1}")
