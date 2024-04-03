from MySQL import *
from income_calculation import *
from tkinter import ttk
import tkinter as tk
import tksheet
mydb = connection_mysql()


# products_mysql(mydb, 3,"kolbász", "csípős kolbász", "1200Ft", 10)
# supplier_mysql(mydb, 20,"Pick", "info@pick.hu", "500", 20)
# orders_mysql(mydb, 1232, 3, 20, 20)

calculate_income(mydb)
calculate_spend(mydb)
calculate_net_income(mydb)


def income():
    mydb = connection_mysql()
    print("Total Income:", calculate_income(mydb))
    print("Total Spend:", calculate_spend(mydb))
    print("Net Income:", calculate_net_income(mydb))
    mydb.close()


def display_data():
    mydb = connection_mysql()
    data = Get_data_orders(mydb)

    for item in tree.get_children():
        tree.delete(item)

    for row in data:
        tree.insert("", "end", values=row)
    mydb.close()

# tkinter_UI_starts here:

root = tk.Tk()
tree = ttk.Treeview(root, columns=("c1", "c2", "c3", "c4", "c5"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="order_id")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="product_id")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="supplier_id")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="quantity")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="order_date")
tree.pack()
button1 = tk.Button(text="Display data", command=lambda: display_data())
button1.pack(pady=10)
button2 = tk.Button(text="Income calculation", command=lambda: income())
button2.pack(pady=10)
root.mainloop()
