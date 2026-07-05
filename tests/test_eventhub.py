from azure_services.eventhub_producer import send_message

message = {
    "prediction": "Benign",
    "confidence": 0.999,
    "protocol": "TCP",
    "source_ip": "10.0.0.10",
    "destination_ip": "172.16.1.5"
}

send_message(message)