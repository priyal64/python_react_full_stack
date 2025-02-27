import pymysql # type: ignore

# Database connection details
host = "localhost"  # Your MySQL server's host
user = "root"  # Your MySQL username
password = "123"  # Your MySQL password
database = "mydatabase"  # The name of the database you want to connect to

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

    # Example: Fetch and display all tables in the database
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table)

except pymysql.MySQLError as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if connection:
        connection.close()
        print("MySQL connection closed.")
