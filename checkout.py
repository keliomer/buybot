





class Checkout(object):

    def __init__(self, bill_address, ship_address=None):
        """ __init__ is used for setting up attributes for a class

        We set up a class to keep information persistent
        this means we can set up a checkou object once and reuse the information in it
        We can also give Checkout different functionality by adding functions
        below __init__
        """
        self.bill = bill_address
        self.ship = bill_address
        if ship_address:
            self.ship = ship_address



class Address(object):
    """Collects address information"""
    def __init__(self, address, city, state, zip):
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        """__str__ will display when you call print Address"""
        string_format = "{address} {city} {state} {zip}".format(address=self.address, city=self.city,
                                                                state=self.state, zip=self.zip)
        return string_format
    def __repr__(self):
        """__repr__ will display if you just call Address in a terminal"""
        string_format = "{address} {city} {state} {zip}".format(address=self.address, city=self.city,
                                                                state=self.state, zip=self.zip)
        return string_format