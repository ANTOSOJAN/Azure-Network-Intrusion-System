from azure_services.sql_database import get_sql_connection

connection = get_sql_connection()
cursor = connection.cursor()

query = """
INSERT INTO predictions
(prediction, confidence, source_ip, destination_ip, protocol)
VALUES (?, ?, ?, ?, ?)
"""

data = (
    "Attack",
    0.982,
    "192.168.1.10",
    "172.16.0.25",
    "TCP"
)

cursor.execute(query, data)

connection.commit()

print("Prediction inserted successfully!")

cursor.close()
connection.close()