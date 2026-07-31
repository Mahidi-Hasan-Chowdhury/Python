# customer, employee, Admin

from abc import ABC
from orders import Order
from menu import Menu
from restaurant import Restaurant
from food_item import FoodItem
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

        self.cart = Order()

    def show_menu(self,restaurant):
        restaurant.Menu.show_menu()
    
    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.Menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Item Quantity Exceeded")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item Not Found.")

    def view_cart(self):
       print("---View Cart---")
       print("Name\tPrice\tQuantity") 
       for item,quantity in self.cart.items.items():
           print(f"{item.name}\t{item.price}\t{quantity}")
           #print(f"Total Price : {self.cart.total_price()}")
           print(f"Total Price : {self.cart.total_price}")
    
    def pay_bill(self):
        print("Total {self.cart.total_price} Paid Successfully")
        self.cart.clear()



class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

#emp1 = Employee("Mahidi","mahidi123@gmail.com",123456,"Dhaka",21,"Chef",20000)  
#print(emp1.name)


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self,Restaurant,employee):
        Restaurant.add_employee(employee)
    
    def view_employee(self,Restaurant):
        Restaurant.view_employee()
    
    def add_menu_item(self,restaurant,item):
        restaurant.Menu.add_menu_item(item)

    def remove_item(self,restaurant,item):
        restaurant.Menu.remove_item(item)
    def view_menu(self,restaurant):
        restaurant.Menu.show_menu()





#admin1 = Admin("Karim","123123","Karim123@gmail.com","Dhaka")
#admin1.add_employee("sagor","sagor123@gmail.com","12345","Rampura","23","Chef","15000")

#admin1.view_employee()

# restaurant1 = Restaurant("Restaurant1")
# menu1 = Menu()
# item1 = FoodItem("Pizza",250,10)
# item2 = FoodItem("Burger",120,20)
# admin1.add_menu_item(restaurant1,item1)
# admin1.add_menu_item(restaurant1,item2)

# Customer1 = Customer("Rahim","Rahim123",12345,"Gulshan")
# Customer1.show_menu(restaurant1)



# Customer1.add_to_cart(restaurant1,item_name,item_quantity)
# Customer1.view_cart()
