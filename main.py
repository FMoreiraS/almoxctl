class Product:
    def __init__(self, name, quantity_stored):
        self.name = name
        self.quantity_stored = quantity_stored

# Product inputs and outputs can be reduced to the same class. Output, however,
# must have a few extra attributes.
class Movement:

    # Builder for inputs
    def __init__(self, date, product_name, quantity):
        self.type = True
        self.date = date
        self.product_name = product_name
        self.quantity = quantity

    # Builder for outputs
    @overload
    def __init__(self, type, responsible, date, product_name, quantity):
        self.type = type
        self.date = date
        self.responsible = responsible
        self.product_name = product_name
        self.quantity = quantity

if __name__ == '__main__':
    print('BEM-VINDO AO ALMOXCTL')