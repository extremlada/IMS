from MySQL import *

mydb = connection_mysql()

products_mysql(mydb, 3,"kolbász", "csípős kolbász", "1200Ft", 10)
supplier_mysql(mydb, 20,"Pick", "info@pick.hu")
orders_mysql(mydb, 1232, 3, 20, 20)