class Product:
    def __init__(self, name, quantity_stored):
        self.name = name
        self.quantity_stored = quantity_stored

# Product inputs and outputs can be reduced to the same class. Output, however,
# must have a few extra attributes.
class Movement:

    # We can use optional parameters to define unique parameters of the outputs.
    def __init__(self, product_name, quantity, date, type=True, responsible=None):
        self.product_name = product_name
        self.quantity = quantity
        self.date = date
        self.type = type
        self.responsible = responsible

if __name__ == '__main__':
    print('BEM-VINDO AO ALMOXCTL')