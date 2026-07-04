from azure.sql_database import get_sql_connection

connection = get_sql_connection()
cursor = connection.cursor()

create_table_query = """
IF NOT EXISTS (
    SELECT * FROM sysobjects
    WHERE name='predictions' AND xtype='U'
)
CREATE TABLE predictions (
    id INT IDENTITY(1,1) PRIMARY KEY,
    timestamp DATETIME DEFAULT GETDATE(),
    prediction VARCHAR(50),
    confidence FLOAT,
    source_ip VARCHAR(50),
    destination_ip VARCHAR(50),
    protocol VARCHAR(20)
)
"""

cursor.execute(create_table_query)

connection.commit()

print("Predictions table created successfully!")

cursor.close()
connection.close()