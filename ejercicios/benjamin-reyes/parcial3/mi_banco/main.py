from banco import Banco
from Cuenta import Cuenta

def main():
    cuenta1 = Cuenta("Fulanito Perez", "001", 1000)
    cuenta2 = Cuenta("Perezcila Sanchea", "002", 500)

    banco = Banco()
    banco.transferir(cuenta1,cuenta2, 500)
    print("Cuenta origen:",cuenta1.saldo)
    print

    if __name__ == "__main__":
        main()