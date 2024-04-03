from MySQL import *


def calculate_income(mydb):
    mycursor = mydb.cursor()

    # Calculate total income
    mycursor.execute("SELECT SUM(price * orders.quantity) AS total_income "
                     "FROM orders "
                     "JOIN products ON orders.product_id = products.product_id")
    total_income = mycursor.fetchone()[0]

    return total_income


def calculate_spend(mydb):
    mycursor = mydb.cursor()

    # Calculate total spend
    mycursor.execute("SELECT SUM(suppliers.price * suppliers.quantity) AS total_spend FROM suppliers")
    total_spend = mycursor.fetchone()[0]

    return total_spend


def calculate_net_income(mydb):
    total_income = calculate_income(mydb)
    total_spend = calculate_spend(mydb)
    net_income = float(total_income) - float(total_spend)
    return net_income
