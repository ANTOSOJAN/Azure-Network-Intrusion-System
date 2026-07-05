import joblib
import pandas as pd

# Load model artifacts once
model = joblib.load("models/best_ids_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


def predict_network_event(event):
    """
    Predict whether a network event is Benign or Attack.
    Returns:
        prediction (0 or 1)
        confidence (0-1)
    """

    # Convert incoming event to DataFrame
    df = pd.DataFrame([event])

    # Remove label columns if present
    df = df.drop(columns=["Label", "Label_Binary"], errors="ignore")

    # Ensure correct feature order
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Scale features
    scaled = scaler.transform(df)

    # Convert back to DataFrame to preserve feature names
    scaled_df = pd.DataFrame(
        scaled,
        columns=feature_columns
    )

    # Make prediction
    prediction = model.predict(scaled_df)[0]

    # Prediction confidence
    confidence = model.predict_proba(scaled_df).max()

    return prediction, confidence