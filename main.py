from datetime import datetime

class Product:
    def __init__(self, name, quantity, date):
        self.name = name
        self.quantity_stored = quantity
        self.date_of_entry = date

    def set_quantity(self, newQuantity):
        self.quantity_stored = newQuantity

# Product entries and exits can be reduced to the same class. Exits, however,
# must have a few extra attributes.
# We can use optional parameters to define unique attributes of the stock exits.
class Movement:
    def __init__(self, product_name, quantity, date, type=True, responsible=None):
        self.product_name = product_name
        self.quantity = quantity
        self.date = date
        # Type in a stock movement can only be entry or exits, so a boolean value
        # can be used to symplify the storage of the field.
        # True = entry; False = exit
        self.type = type
        self.responsible = responsible

class Main:
    global stored_products
    stored_products = []
    global stock_movements
    stock_movements = []
    @staticmethod
    def main():
        print('BEM-VINDO AO ALMOXCTL')
    
        while True:
            print('1. Adicionar produto no estoque')
            print('2. Retirar produto do estoque')
            print('3. Exibir produtos em estoque')
            print('4. Exibir movimentações no estoque')
            print('5. Sair')
            
            option = 0
            try:
                option = int(input())
            except ValueError:
                print('Valor inadequado. Tente um número de 1 a 5')


            match option:
                case 1:
                    print(Main.add_product(stored_products))
                case 2:
                    print(Main.remove_product(stored_products))
                case 3:
                    Main.show_products(stored_products)
                case 4:
                    Main.show_stock_movements(stock_movements)
                case 5:
                    print('Programa encerrado')
                    break
                # case _:
                #     print('Opção inválida')

    @staticmethod
    def add_product(stored_products: list[Product]):
        success_msg = 'Produto adicionado com sucesso\n'
        # If there is any product in stock, the user can add more of it.
        if len(stored_products) > 0:
            option = input('Deseja adicionar um produto já existente?(s/n) ')
            if option == 's' or option == 'S':
                Main.show_products(stored_products)
                product_modified = None
                product_name = input('Digite o nome do produto que será adicionado:')
                # Ensuring the product exists in stock
                for p in stored_products:
                    if p.name == product_name:
                        product_modified = p
                if product_modified == None: return 'O produto indicado não está no estoque\n'
                
                print('Digite a quantidade a ser adicionada:')
                quantity = Main.validate_quantity()
                new_quantity = product_modified.quantity_stored + quantity
                product_modified.set_quantity(new_quantity)
                return success_msg
        
        product_name = input('Digite o nome do produto que será adicionado: ')
        print('Digite a quantidade a ser adicionada:')
        quantity = Main.validate_quantity()
        # If the entry date of a product is not the same as the time of registration
        # in the system, the user could enter the date manually, this way:
        # entry_date = input('Digite a data da inserção do produto: ')
        entry_date = datetime.today().strftime('%d/%m/%Y')
        product_added = Product(product_name, quantity, entry_date)
        stored_products.append(product_added)
        Main.add_movement(stock_movements, product_name, quantity)
        return success_msg


    @staticmethod
    def remove_product(stored_products: list):
        if len(stored_products) > 0:
            product_to_remove = None

            Main.show_products(stored_products)
            print('Digite o nome de um dos produtos em estoque para removê-lo')
            product_name = input()

            # Ensuring that the product exists in stock
            for p in stored_products:
                if p.name == product_name: product_to_remove = p
            if product_to_remove == None: return 'O produto indicado não está no estoque\n'
            
            current_quantity = product_to_remove.quantity_stored
            print('Digite a quantidade que deseja remover')
            quantity_to_remove = Main.validate_quantity()
            if quantity_to_remove > current_quantity:
                return 'A quantidade em estoque é menor que a solicitada\n'
            elif quantity_to_remove == current_quantity:
                stored_products.remove(product_to_remove)
            product_to_remove.set_quantity(current_quantity - quantity_to_remove)
            Main.add_movement(stock_movements, product_name, quantity_to_remove, False)
            return 'Produto removido com sucesso\n'
        else:
            return 'Não há produtos no estoque\n'


    @staticmethod
    def add_movement(movement_list: list, product_name, quantity, type=True):
        responsible_name = ' '
        if type == False:
            print('Digite o nome do responsável pela retirada:')
            responsible_name = input()
        # Stock movements will receive the date of the moment the movements are made.
        current_date = datetime.today().strftime('%d/%m/%Y')
        movement_to_add = Movement(product_name, quantity, current_date, type, responsible_name)
        movement_list.append(movement_to_add)

    @staticmethod
    def show_products(products: list):
        if len(products) > 0:
            print('-' * 20)
            print('PRODUTOS EM ESTOQUE')
            for p in products:
                print(f'{p.quantity_stored} | {p.date_of_entry} | {p.name}')
                if p == products[len(products) - 1]: print()
        else:
            print('Não há produtos em estoque\n')

    @staticmethod
    def show_stock_movements(movements: list):
        if len(movements) > 0:
            print('-' * 20)
            print('MOVIMENTAÇÕES NO ESTOQUE')
            for m in movements:
                # Ternary operator returns a textual value of movement's type
                # because the attribute is a boolean value
                type = 'entrada' if m.type else ' saída '

                print(f'{m.date} | {type} | {m.quantity} | {m.product_name} | {m.responsible}')
                if m == movements[len(movements) - 1]: print()
        else:
            print('Não foram feitas movimentações no estoque')

    @staticmethod
    def validate_quantity():
        quantity = 0
        while not quantity >= 1:
            try:
                quantity = int(input())
                return quantity
            except ValueError:
                print('Quantidade inválida')

    # Searches for a product by name, ensuring that the product exists in stock
    @staticmethod
    def find_product(product_name):
        product_to_found = None
        for p in stored_products:
            if p.name == product_name: product_to_found = p
        return product_to_found

# Calls Main to run the system
Main.main()
