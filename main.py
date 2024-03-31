from MySQL import *
from income_calculation import *
mydb = connection_mysql()

#products_mysql(mydb, 3,"kolbász", "csípős kolbász", "1200Ft", 10)
#supplier_mysql(mydb, 20,"Pick", "info@pick.hu", "500", 20)
#orders_mysql(mydb, 1232, 3, 20, 20)

calculate_income(mydb)
calculate_spend(mydb)
calculate_net_income(mydb)

mydb = connection_mysql()
print("Total Income:", calculate_income(mydb))
print("Total Spend:", calculate_spend(mydb))
print("Net Income:", calculate_net_income(mydb))
mydb.close()
