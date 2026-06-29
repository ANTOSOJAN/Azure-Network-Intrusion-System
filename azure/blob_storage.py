import os
from io import BytesIO

import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
BLOB_NAME = os.getenv("BLOB_NAME")


def load_dataset_from_azure():
    try:
        # Create Blob Service Client
        blob_service_client = BlobServiceClient.from_connection_string(
            CONNECTION_STRING
        )

        # Create Blob Client
        blob_client = blob_service_client.get_blob_client(
            container=CONTAINER_NAME,
            blob=BLOB_NAME
        )

        print("Downloading dataset from Azure...")

        # Download file
        blob_data = blob_client.download_blob()

        # Read bytes
        data = blob_data.readall()

        print("Download successful!")

        # Load into pandas
        df = pd.read_csv(BytesIO(data))

        print(f"Dataset loaded successfully. Shape: {df.shape}")

        return df

    except Exception as e:
        print(f"Error: {e}")
        raise