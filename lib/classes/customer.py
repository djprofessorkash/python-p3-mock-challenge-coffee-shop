"""
[OOPD] Customer Object Design:

    • One Customer has Many Orders. 
        --> One-to-Many
    • One Coffee can have Many Customers
        AND
      One Customer can have Many Coffees.
        --> Many-to-Many

[OOPD] Customer Class: Initialization/Properties.

    • METHOD: `Customer.__init__(self, name)`
        --> Customer should be initialized with a name
    • PROPERTY: `Customer.name`
        --> PROPERTY INITIALIZATION: `@property`
            --> Returns name
        --> PROPERTY SETTER: `@name.setter`
            --> Names must be of type str
            --> Names must be between 1 and 15 characters, inclusive
            --> If you are using exceptions, uncomment lines 26-27 and 34-38 in customer_test.py.
                --> raise Exception if setter fails

[OOPD] Customer Class: Relationships: Basic Methods/Properties.

    • METHOD: `Customer.orders(self, new_order=None)`
        --> Adds new orders to customer
        --> Returns a list of all orders a customer has ordered
        --> orders must be of type `Order`
        --> Will be called from `Order.__init__`

    • METHOD: `Customer.coffees(self, new_coffee=None)`
        --> Adds new coffees to customer
        --> Returns a unique list of all coffees a customer has ordered.
        --> Coffees must be of type `Coffee`
        --> Will be called from `Order.__init__`

[OOPD] Customer Class: Relationships: Aggregate/Associative Methods.

    • METHOD: `Customer.create_order(self, coffee, price)`
        --> Given a coffee object and a price (as an integer), creates a new order and associates it with that customer and coffee.
"""

class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass