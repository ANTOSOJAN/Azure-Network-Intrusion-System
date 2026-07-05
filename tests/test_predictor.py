from azure_services.blob_storage import load_dataset_from_azure
from azure_services.ml_predictor import predict_network_event

df = load_dataset_from_azure()

sample = df.iloc[0].to_dict()

prediction, confidence = predict_network_event(sample)

print("\nPrediction:", prediction)
print("Confidence:", confidence)