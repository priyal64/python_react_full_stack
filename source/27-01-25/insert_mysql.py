import pymysql # type: ignore

# Database connection details
host = "localhost"
user = "root"
password = "123"
database = "mydatabase"

try:
    # Establish a connection to MySQL
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connection to MySQL database successful!")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example: Insert a new row into a table
    # Replace 'your_table_name' and column names with your actual table details
    insert_query = """
    INSERT INTO customer (id, name, age,occupation)
    VALUES (%s, %s, %s,%s);
    """
    data_to_insert = (1, "Priyal", 21, "Engineer")

    # Execute the query
    cursor.execute(insert_query, data_to_insert)

    # Commit the transaction
    connection.commit()
    print(f"{cursor.rowcount} record(s) inserted successfully.")

except pymysql.MySQLError as e:
    print(f"Error inserting data into MySQL: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
        print("MySQL connection closed.")
