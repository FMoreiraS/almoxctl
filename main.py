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

class Main:
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
                case _:
                    print('Opção inválida')

    @staticmethod
    def addProduct():
        print('Produto adicionado com sucesso')

    @staticmethod
    def removeProduct():
        print('Produto removido com sucesso')

if __name__ == '__main__':
    Main.main()
