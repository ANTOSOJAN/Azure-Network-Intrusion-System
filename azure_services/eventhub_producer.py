"""
Azure Event Hub Producer

Streams network traffic records to Azure Event Hubs.
"""

import os
import json

from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

from azure_services.blob_storage import load_dataset_from_azure

load_dotenv()

CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")


def get_producer():
    return EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )


def send_dataset(limit=20):

    print("Loading dataset from Azure Blob Storage...\n")

    df = load_dataset_from_azure()

    producer = get_producer()

    count = 0

    for _, row in df.iterrows():

        event = row.to_dict()

        batch = producer.create_batch()

        batch.add(EventData(json.dumps(event, default=str)))

        producer.send_batch(batch)

        count += 1

        print(f"Sent Event {count}")

        if count >= limit:
            break

    producer.close()

    print("\nStreaming completed!")