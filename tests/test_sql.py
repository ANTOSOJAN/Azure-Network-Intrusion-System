from azure_services.sql_database import get_sql_connection

try:
    print("Connecting to Azure SQL Database...\n")

    connection = get_sql_connection()

    print("\nConnection Successful!")

    cursor = connection.cursor()

    cursor.execute("SELECT @@VERSION")

    row = cursor.fetchone()

    print("\nAzure SQL Server Version:\n")
    print(row[0])

    cursor.close()
    connection.close()

    print("\nConnection Closed Successfully.")

except Exception as e:
    print("\nConnection Failed!")
    print(e)