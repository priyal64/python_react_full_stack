import mysql.connector
def connect_db():
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='mydatabase'
    )
    print('db connected')
    return connection
def insert_db(connection):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO customer (id, name, age,occupation)
    VALUES (%s, %s, %s,%s);
    """
    data_to_insert = (1, "Priyal", 21, "Engineer")
    cursor.execute(insert_query, data_to_insert)
    connection.commit()
    # print(f"{cursor.rowcount} record(s) inserted successfully.")
def print_db(connection):
    cursor = connection.cursor()
    select_query=""" SELECT * FROM customer;"""
    cursor.execute(select_query)
    connection.commit()
    
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)

def main():
    c=connect_db()
    insert_db(c)
    print_db(c)

main()