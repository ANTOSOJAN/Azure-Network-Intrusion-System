from azure.sql_database import get_sql_connection

connection = get_sql_connection()
cursor = connection.cursor()

cursor.execute("""
SELECT
    id,
    timestamp,
    prediction,
    confidence,
    source_ip,
    destination_ip,
    protocol
FROM predictions
ORDER BY id DESC;
""")

rows = cursor.fetchall()

print("\nStored Predictions\n")
print("-" * 90)

for row in rows:
    print(
        f"ID: {row.id} | "
        f"Time: {row.timestamp} | "
        f"Prediction: {row.prediction} | "
        f"Confidence: {row.confidence:.3f} | "
        f"Source: {row.source_ip} | "
        f"Destination: {row.destination_ip} | "
        f"Protocol: {row.protocol}"
    )

cursor.close()
connection.close()