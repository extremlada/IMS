import mysql.connector

products = False
suppliers = False
orders = False





def connection_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="raktar",
    )
    return mydb


def products_mysql(mydb, product_id, name, description, price, quantity):
    mycursor = mydb.cursor()

    # ez egy formula a %s place holderek

    ProductsFormula = ("INSERT INTO products (product_id, name, description, price, quantity) "
                       "VALUES (%s, %s, %s, %s, %s)")

    # igy használjuk a formulat

    mycursor.execute(ProductsFormula, (product_id, name, description, price, quantity))

    # ezzel tudjuk menteni a changeket!!!!!!!!
    mydb.commit()


def supplier_mysql(mydb, supplier_id, name, contact_info, price, quantity):
    mycursor = mydb.cursor()

    # ez egy formula a %s place holderek

    SupplierFormula = "INSERT INTO suppliers (supplier_id, name, contact_info, price, quantity) VALUES (%s, %s, %s, %s, %s)"

    # igy használjuk a formulat

    mycursor.execute(SupplierFormula, (supplier_id, name, contact_info, price, quantity))

    # ezzel tudjuk menteni a changeket!!!!!!!!
    mydb.commit()


def orders_mysql(mydb, order_id, product_id, supplier_id, quantity):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) FROM products WHERE product_id = %s", (product_id,))
    product_exists = mycursor.fetchone()[0]

    mycursor.execute("SELECT COUNT(*) FROM suppliers WHERE supplier_id = %s", (supplier_id,))
    supplier_exists = mycursor.fetchone()[0]

    if not product_exists:
        raise ValueError(f"Product with ID {product_id} does not exist")

    if not supplier_exists:
        raise ValueError(f"Supplier with ID {supplier_id} does not exist")

    # Define the SQL query with placeholders
    OrderFormula = ("INSERT INTO orders (order_id, product_id, supplier_id, quantity, order_date) "
                    "VALUES (%s, %s, %s, %s, NOW())")

    # Execute the query and pass the arguments as a tuple
    mycursor.execute(OrderFormula, (order_id, product_id, supplier_id, quantity))

    # Commit the changes to the database
    mydb.commit()


connection_mysql()
