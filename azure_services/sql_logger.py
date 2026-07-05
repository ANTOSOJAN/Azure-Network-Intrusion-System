"""
Azure SQL Logger

Stores ML prediction results in Azure SQL Database.
"""

from azure_services.sql_database import get_sql_connection

connection = None
cursor = None


def get_cursor():
    global connection, cursor

    if connection is None:
        connection = get_sql_connection()
        cursor = connection.cursor()

    return cursor


def log_prediction(prediction, confidence, event_data):

    cursor = get_cursor()

    query = """
    INSERT INTO predictions
    (
        prediction,
        confidence,
        protocol,
        destination_port,
        flow_duration
    )
    VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(
        query,
        (
            str(prediction),
            float(confidence),
            int(event_data.get("Protocol", 0)),
            int(event_data.get("Dst Port", 0)),
            int(event_data.get("Flow Duration", 0))
        )
    )

    connection.commit()


def close_connection():
    global connection, cursor

    if cursor:
        cursor.close()

    if connection:
        connection.close()