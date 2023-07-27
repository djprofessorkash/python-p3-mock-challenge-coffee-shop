"""
[OOPD] Coffee Object Design:

    • One Coffee has Many Orders. 
        --> One-to-Many
    • One Coffee can have Many Customers
        AND
      One Customer can have Many Coffees.
        --> Many-to-Many

[OOPD] Coffee Class: Initialization/Properties.

    • METHOD: `Coffee.__init__(self, name)`
        --> Coffee should be initialized with a name
    • PROPERTY: `Coffee.name`
        --> PROPERTY INITIALIZATION: `@property`
            --> Returns the coffee's name
        --> PROPERTY SETTER: `@name.setter`
            --> Should not be able to change after the coffee is created
                --> Hint: `hasattr()`
            --> If you are using exceptions, uncomment lines 24-25 in coffee_test.py.
                --> `raise Exception` if setter fails

[OOPD] Coffee Class: Relationships: Basic Methods/Properties.

    • METHOD: `Coffee.orders(self, new_order=None)`
        --> Adds new orders to coffee
        --> Returns a list of all orders for that coffee
        --> orders must be of type `Order`
        --> Will be called from `Order.__init__`

    • METHOD: `Coffee.customers(self, new_customer=None)`
        --> Adds new customers to coffee
        --> Returns a unique list of all customers who have ordered a particular coffee.
        --> Customers must be of type `Customer`
        --> Will be called from `Order.__init__`

[OOPD] Coffee Class: Relationships: Aggregate/Associative Methods.

    • METHOD: `Coffee.num_orders(self)`
        --> Returns the total number of times that coffee has been ordered
    
    • METHOD: `Coffee.average_price(self)`
        --> Returns the average price for a coffee based on its orders
            --> Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
"""

class Coffee:
    def __init__(self, name):
        self.name = name
        
    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass