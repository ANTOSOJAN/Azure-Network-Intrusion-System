from azure_services.blob_storage import load_dataset_from_azure

try:
    df = load_dataset_from_azure()

    print("\nFirst 5 rows:")
    print(df.head())

except Exception as e:
    print("\nException occurred:")
    print(type(e).__name__)
    print(e)