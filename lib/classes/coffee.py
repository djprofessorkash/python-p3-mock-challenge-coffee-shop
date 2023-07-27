"""
[OOPD] Coffee Object Design:

    • One Coffee has Many Orders. 
        --> One-to-Many
    • One Coffee can have Many Customers
        AND
      One Customer can have Many Coffees.
        --> Many-to-Many

[OOPD] Coffee Class: Initialization/Properties.

    • INITIALIZER: `Coffee.__init__(self, name)`
        --> Coffee should be initialized with a name
    • PROPERTY: `Coffee.name`
        --> PROPERTY INITIALIZATION: `@property; def name(self)`
            --> Returns the coffee's name
        --> PROPERTY SETTER: `@name.setter`
            --> Should not be able to change after the coffee is created
                --> Hint: `hasattr()`
            --> If you are using exceptions, uncomment lines 24-25 in coffee_test.py.
                --> `raise Exception` if setter fails

[OOPD] Coffee Class: Relationships: Basic Methods/Properties.

    • METHOD: `Coffee.orders(self, new_order=None)`
        --> Adds `new_order` to `Coffee`'s orders
        --> Returns a list of all orders for that coffee
        --> orders must be of type `Order`
        --> Will be called from `Order.__init__`

    • METHOD: `Coffee.customers(self, new_customer=None)`
        --> Adds new customers to coffee
        --> Returns a list of all unique customers who have ordered a particular coffee (i.e. the list will not contain the same customer more than once).
            --> The list must only contain objects of type `Customer`
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
        # A coffee has many orders.
        self._orders = []
        # A coffee has many customers.
        self._customers = []

    # Initialize Property: `Coffee.name`
    @property
    def name(self):
        return self._name
    
    # Functionalize Property with Setter: `Coffee.name`
    @name.setter
    def name(self, name):
        # Create validations for data type (str) and existence of property
        NAME_IS_STR = (type(name) == str)
        NAME_EXISTS = (not hasattr(self, "name"))
        
        # Conditionally validate property to set property
        if NAME_IS_STR and NAME_EXISTS:
            self._name = name
        else:
            raise Exception("`Coffee.name` already exists!")
        
    # Add functionality to `Coffee.orders()`
    def orders(self, new_order=None):
        from classes.order import Order

        # Create validations for data type (Order) and instantiation of property
        ORDER_IS_INSTANTIATED = (new_order is not None)
        ORDER_IS_ORDER = (isinstance(new_order, Order))

        # Conditionally validate property to extend property list
        if ORDER_IS_INSTANTIATED and ORDER_IS_ORDER:
            self._orders.append(new_order)
        return self._orders
    
    # Add functionality to `Coffee.customers()`
    def customers(self, new_customer=None):
        from classes.customer import Customer

        # Create validations for data type (Customer) and uniqueness of property
        CUSTOMER_IS_UNIQUE = (new_customer not in self._customers)
        CUSTOMER_IS_CUSTOMER = (isinstance(new_customer, Customer))

        # Conditionally validate property to extend property list
        if CUSTOMER_IS_UNIQUE and CUSTOMER_IS_CUSTOMER:
            self._customers.append(new_customer)
        return self._customers
    
    # Add functionality to `Coffee.num_orders()`
    def num_orders(self):
        # Return length of orders property list
        return len(self._orders)
    
    # Add functionality to `Coffee.average_price()`
    def average_price(self):
        # Calculate total price across all orders
        total_price = 0
        for order in self._orders:
            total_price += order.price
        # Return average price (total price divided by number of orders)
        return total_price / len(self._orders)
        """ We can also do this... """
        return total_price / self.num_orders()
        """ ...and this... """
        return sum([order.price for order in self_orders]) / self.num_orders()