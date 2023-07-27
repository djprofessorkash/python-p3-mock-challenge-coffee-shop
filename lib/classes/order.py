"""
[OOPD] Customer Object Design:

    • One Coffee has Many Orders. 
        --> One-to-Many
    • One Customer has Many Orders. 
        --> One-to-Many
    • An Order belongs to a Customer and to a Coffee.

[OOPD] Order Class: Initialization/Properties.

    • INITIALIZER: `Order.__init__(self, customer, coffee, price)`
        --> Orders should be initialized with a customer, coffee, and a price (a number)
    • PROPERTY: `Order.price`
        --> PROPERTY INITIALIZATION: `@property; def price(self)`
            --> Returns the price for a coffee
        --> PROPERTY SETTER: `@price.setter; def price(self, price)`
            --> Returns the price for a coffee
            --> Price must be a number between 1 and 10, inclusive
                --> `raise Exception` if setter fails
    • PROPERTY: `Order.customer`
        --> PROPERTY INITIALIZATION: `@property; def customer(self)`
            --> Returns the customer object for that order
        --> PROPERTY SETTER: `@customer.setter; def customer(self, customer)`
            --> Must be of type Customer
                --> `raise Exception` if setter fails
    • PROPERTY: `Order.coffee`
        --> PROPERTY INITIALIZATION: `@property; def coffee(self)`
            --> Returns the coffee object for that order
        --> PROPERTY SETTER: `@coffee.setter; def coffee(self, coffee)`
            --> Must be of type Coffee
                --> `raise Exception` if setter fails

[OOPD] Order Class: Relationships: Basic Methods/Properties.
"""
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
