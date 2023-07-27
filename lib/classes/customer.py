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
        # A customer has many orders.
        self._orders = []
        # A customer has many coffees.
        self._coffees = []

    # Initialize Property: `Customer.name`
    @property
    def name(self):
        return self._name
    
    # Functionalize Property with Setter: `Customer.name`
    @name.setter
    def name(self, name):
        # Create validations for data type (str) and length requirements of property
        NAME_IS_STR = (isinstance(name, str))
        NAME_IS_WITHIN_ACCEPTABLE_LENGTH = (1 <= len(name) <= 15)
        
        # Conditionally validate property to set property
        if NAME_IS_STR and NAME_IS_WITHIN_ACCEPTABLE_LENGTH:
            self._name = name
        else:
            raise Exception("Unacceptable data format for `Customer.name`!")
        
    # Add functionality to `Customer.orders()`
    def orders(self, new_order=None):
        from classes.order import Order

        # Create validations for data type (Order) and instantiation of property
        ORDER_IS_INSTANTIATED = (new_order is not None)
        ORDER_IS_ORDER = (isinstance(new_order, Order))

        # Conditionally validate property to extend property list
        if ORDER_IS_INSTANTIATED and ORDER_IS_ORDER:
            self._orders.append(new_order)
        return self._orders
    
    # Add functionality to `Customer.coffees()`
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee

        # Create validations for data type (Coffee) and uniqueness of property
        COFFEE_IS_UNIQUE = (new_coffee not in self._coffees)
        COFFEE_IS_COFFEE = (isinstance(new_coffee, Coffee))

        # Conditionally validate property to extend property list
        if COFFEE_IS_UNIQUE and COFFEE_IS_COFFEE:
            self._coffees.append(new_coffee)
        return self._coffees