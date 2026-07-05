"""
Azure Event Hub Consumer

Receives streaming network traffic from Azure Event Hubs,
predicts whether the traffic is Benign or Attack using the
trained Gradient Boosting model, and stores the prediction
results in Azure SQL Database.
"""

import json
import os

from dotenv import load_dotenv
from azure.eventhub import EventHubConsumerClient

from azure_services.ml_predictor import predict_network_event
from azure_services.sql_logger import (
    log_prediction,
    close_connection
)

# Load environment variables
load_dotenv()

CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")
CONSUMER_GROUP = "$Default"


def on_event(partition_context, event):
    """
    Process each incoming Event Hub message.
    """

    try:

        # Convert Event Hub message to dictionary
        event_data = json.loads(event.body_as_str(encoding="UTF-8"))

        # Run ML prediction
        prediction, confidence = predict_network_event(event_data)

        prediction_label = (
            "Attack"
            if prediction == 1
            else "Benign"
        )

        # Store prediction in Azure SQL
        log_prediction(
            prediction_label,
            confidence,
            event_data
        )

        print("\n" + "=" * 70)
        print(" Network Event Processed")
        print("=" * 70)
        print(f"Prediction       : {prediction_label}")
        print(f"Confidence       : {confidence:.4f}")
        print(f"Protocol         : {event_data.get('Protocol')}")
        print(f"Destination Port : {event_data.get('Dst Port')}")
        print(f"Flow Duration    : {event_data.get('Flow Duration')}")
        print("Status           : Stored in Azure SQL Database")
        print("=" * 70)

        # Save Event Hub checkpoint
        partition_context.update_checkpoint(event)

    except Exception as e:
        print(f"\n[ERROR] {e}")


def main():
    """
    Start listening for Event Hub messages.
    """

    client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        consumer_group=CONSUMER_GROUP,
        eventhub_name=EVENT_HUB_NAME
    )

    print("\nListening for network events...\n")

    try:
        with client:
            client.receive(
                on_event=on_event,
                starting_position="@latest"
            )

    except KeyboardInterrupt:
        print("\nStopped listening for events.")

    finally:
        close_connection()
        print("SQL connection closed.")


if __name__ == "__main__":
    main()