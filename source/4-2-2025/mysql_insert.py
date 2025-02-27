import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123',
            database='mydatabase'
        )
        print("Database is connected....")
        return connection
    except mysql.connector.Error as e:
        print("Something went wrong connecting to the database.", e)  
        return None

def create_table(connection):
    cursor = connection.cursor()
    try:
        query = """
        CREATE TABLE IF NOT EXISTS employee (  -- Added IF NOT EXISTS
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            salary INT
        );
        """
        cursor.execute(query)
        connection.commit()  # Commit after successful table creation
        print("Table created successfully!")
    except mysql.connector.Error as e:
        print("Something went wrong creating the table.", e)
    finally:
        cursor.close()

def insert_data(connection):
    cursor = connection.cursor()
    try:
        query = """INSERT INTO employee (name, age, salary) VALUES (%s, %s, %s);"""
        n = int(input("Enter the number of records to be inserted: "))
        data = []
        for _ in range(n):
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = int(input("Enter employee salary: "))
            data.append((name, age, salary))

        cursor.executemany(query, data)
        connection.commit()  # Commit after all inserts are done
        print(f"{n} records inserted successfully!")

    except mysql.connector.Error as e:
        connection.rollback()
        print("Something went wrong inserting data.", e)
    finally:
        cursor.close()

def select_db(connection):
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM employee;"""
        cursor.execute(query)
        myresult = cursor.fetchall()

        for row in myresult: 
            print(row)

    except mysql.connector.Error as e:
        print("Something went wrong selecting data.", e)
    finally:
        cursor.close()


def delete_data(connection):
    cursor = connection.cursor()
    try:
        query = "DELETE FROM employee WHERE id = %s;"
        id_to_delete = int(input("Enter the ID of the employee to delete: "))

        cursor.execute(query, (id_to_delete,)) 
        connection.commit()

        if cursor.rowcount > 0:
            print(f"{cursor.rowcount} record(s) deleted successfully!")
        else:
            print("No record found with that ID.")

    except mysql.connector.Error as e:
        connection.rollback()
        print("Something went wrong deleting data.", e)
    except ValueError:
        print("Invalid input. Please enter an integer ID.")
    finally:
        cursor.close()
def drop_table(connection):
    cursor = connection.cursor()
    try:
        table_name = input("Enter the name of the table to drop: ")
        query = f"DROP TABLE IF EXISTS {table_name};"  
        cursor.execute(query)
        connection.commit()

        print(f"Table '{table_name}' dropped successfully!")

    except mysql.connector.Error as e:
        connection.rollback()
        print(f"Something went wrong dropping the table '{table_name}'.", e)
    finally:
        cursor.close()

def main():
    connection = connect_db()
    if connection is None:
        return  

    # create_table(connection) 
    insert_data(connection)
    select_db(connection)
    # delete_data(connection) 
    # select_db(connection) 
    # drop_table(connection)  
    connection.close()
    print("MySQL connection closed.")

if __name__ == "__main__":
    main()