# #!/usr/bin/env python
# from sqlalchemy import create_engine

# # Snowflake connection parameters
# user = 'NITHIN'
# password = 'Nj@9390779404'
# account_identifier = 'ctkbbdn-xc60080'

# # Create the engine
# engine = create_engine(
#     f'snowflake://{user}:{password}@{account_identifier}/'
# )

# try:
#     # Connect to Snowflake
#     with engine.connect() as connection:
#         # Execute a query
#         results = connection.execute('select current_version()').fetchone()
#         print(results[0])

# finally:
#     # Clean up resources
#     engine.dispose()


# import snowflake.connector

# try:
#     ctx = snowflake.connector.connect(
#         user='NITHIN',
#         password='Nj@9390779404',
#         account='ctkbbdn-xc60080',
#     )
#     print("Connected to Snowflake")
#     cursor = ctx.cursor()
#     cursor.execute("SELECT CURRENT_VERSION()")
#     version = cursor.fetchone()
#     print("Snowflake version:", version[0])

# except snowflake.connector.errors.Error as e:
#     print("Failed to connect to Snowflake:", e)

# finally:
#     if ctx is not None and ctx.is_connected():
#         ctx.close()
#         print("Connection closed")


import snowflake.connector
import os

# Optionally, load credentials from environment variables
user = os.getenv('SNOWFLAKE_USER', 'NITHIN')
password = os.getenv('SNOWFLAKE_PASSWORD', 'Nj@9390779404')
account = os.getenv('SNOWFLAKE_ACCOUNT', 'ctkbbdn-xc60080')

try:
    # Connect to Snowflake
    ctx = snowflake.connector.connect(
        user=user,
        password=password,
        account=account
    )

    cs = ctx.cursor()

    # Create a new schema for client data
    try:
        cs.execute("CREATE SCHEMA IF NOT EXISTS client_data_schema")
        print("Schema created successfully.")
    except Exception as e:
        print(f"Error creating schema: {e}")

    # Create a new table for client data
    try:
        cs.execute("""
            CREATE TABLE IF NOT EXISTS client_data_schema.clients (
                client_id STRING PRIMARY KEY,
                client_name STRING,
                client_email STRING,
                client_phone STRING,
                client_address STRING,
                client_registration_date DATE
            )
        """)
        print("Table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

    # Insert a new client record
    try:
        cs.execute("""
            INSERT INTO client_data_schema.clients (client_id, client_name, client_email, client_phone, client_address, client_registration_date) 
            VALUES ('1', 'Jane Smith', 'jane.smith@example.com', '555-123-4567', '456 Elm St, Anytown, USA', '2024-07-15')
        """)
        print("Client inserted successfully.")
    except Exception as e:
        print(f"Error inserting client: {e}")

    # Query the client records
    try:
        cs.execute("SELECT * FROM client_data_schema.clients")
        clients = cs.fetchall()
        print(f"Number of clients: {len(clients)}")
        for client in clients:
            print(client)
    except Exception as e:
        print(f"Error querying clients: {e}")

    # Close the cursor and connection
    cs.close()
    ctx.close()

except snowflake.connector.errors.DatabaseError as db_err:
    print(f"Database error: {db_err}")
except Exception as e:
    print(f"General error: {e}")
