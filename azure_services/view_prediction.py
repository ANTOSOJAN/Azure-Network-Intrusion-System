from azure_services.sql_database import get_sql_connection

connection = get_sql_connection()

cursor = connection.cursor()

cursor.execute("""
SELECT
    id,
    timestamp,
    prediction,
    confidence,
    protocol,
    destination_port,
    flow_duration
FROM predictions
ORDER BY id DESC;
""")

rows = cursor.fetchall()

print("\nStored Predictions\n")
print("-" * 120)

for row in rows:
    print(
        f"ID: {row.id} | "
        f"Time: {row.timestamp} | "
        f"Prediction: {row.prediction} | "
        f"Confidence: {row.confidence:.3f} | "
        f"Protocol: {row.protocol} | "
        f"Dst Port: {row.destination_port} | "
        f"Flow Duration: {row.flow_duration}"
    )

cursor.close()
connection.close()