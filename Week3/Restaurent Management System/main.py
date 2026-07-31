from food_item import FoodItem
from menu import Menu
from user import  Customer,Admin,Employee
from restaurant import Restaurant
from orders import Order

def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    customer1 = Customer(name=name, email=email, phone=phone, address=address)

    restaurant1 = Restaurant("Restaurant No. 01")

    while True:
        print(f"Welcome {customer1.name}")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer1.show_menu(restaurant1)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer1.add_to_cart(restaurant1,item_name,item_quantity)
        elif choice == 3:
            customer1.view_cart()
        elif choice == 4:
            customer1.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


    
def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    admin1 = Admin(name=name, email=email, phone=phone, address=address)

    restaurant1 = Restaurant("Restaurant No. 01")

    while True:
        print(f"Welcome {admin1.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)

            admin1.add_menu_item(restaurant1,item)
        elif choice == 2:
            name = input("Enter Employee Name: ")
            phone = input("Enter Employee Phone: ")
            email = input("Enter Employee Email: ")
            designation = input("Enter Employee Designation: ")
            age = input("Enter Employee Age: ")
            salary = input("Enter Employee Salary: ")
            address = input("Enter Employee Address: ")
            employee = Employee(name,email,phone,address,age,designation,salary)
            admin1.add_employee(restaurant1,employee)
        elif choice == 3:
            admin1.view_employee(restaurant1)
        elif choice == 4:
            admin1.view_menu(restaurant1)
        elif choice == 5:
            admin1.remove_item(restaurant1,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")



while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")