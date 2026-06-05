class Product:
    def __init__(self, name, quantity, date):
        self.name = name
        self.quantity_stored = quantity
        self.date_of_entry = date

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

class Main:
    @staticmethod
    def main():
        stored_products = []
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
                    Main.addProduct()
                case 2:
                    Main.removeProduct()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print('Programa encerrado')
                    break
                # case _:
                #     print('Opção inválida')

    @staticmethod
    def addProduct(stored_products: list[Product]):
        if len(stored_products) > 0:
            option = input('Deseja adicionar um produto já existente?(s/n) ')
            if option == 's' or option == 'S':
                Main.showProducts(stored_products)
            print('Produto adicionado com sucesso\n')
        
        product_name = input('Digite o nome do produto que será adicionado: ')
        quantity = input('Digite a quantidade a ser adicionada: ')
        entry_date = input('Digite a data da inserção do produto: ')
        product_added = Product(product_name, quantity, entry_date)
        stored_products.append(product_added)
        print('Produto adicionado com sucesso\n')


    @staticmethod
    def removeProduct():
        print('Produto removido com sucesso')

    @staticmethod
    def showProducts(products: list):
        if len(products) > 0:
            print('Produtos em estoque')
            for p in products:
                print(f'{p.quantity_stored} | {p.name}')
                # print('-' * 20)
                # print(p.name)
                # print(p.quantity_stored)
        else:
            print('Não há produtos em estoque')

if __name__ == '__main__':
    Main.main()
