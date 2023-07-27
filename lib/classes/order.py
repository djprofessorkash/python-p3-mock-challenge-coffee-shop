"""
[OOPD] Customer Object Design:

    • One Coffee has Many Orders. 
        --> One-to-Many
    • One Customer has Many Orders. 
        --> One-to-Many
    • An Order belongs to a Customer and to a Coffee.

[OOPD] Order Class: Initialization/Properties.

    • METHOD: `Order.__init__(self, customer, coffee, price)`
        --> Orders should be initialized with a customer, coffee, and a price (a number)
    • PROPERTY: `Order.price`
        --> PROPERTY INITIALIZATION: `@property`
            --> Returns the price for a coffee
        --> PROPERTY SETTER: `@price.setter`
            --> Returns the price for a coffee
            --> Price must be a number between 1 and 10, inclusive
                --> `raise Exception` if setter fails

[OOPD] Order Class: Relationships: Basic Methods/Properties.

    • METHOD: `Order.customer(self, new_customer=None)`
        --> Returns the customer object for that order
        --> Must be of type Customer
            --> `raise Exception` if setter fails

    • METHOD: `Order.coffee(self, new_coffee=None)`
        --> Returns the coffee object for that order
        --> Must be of type Coffee
            --> `raise Exception` if setter fails
"""
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
