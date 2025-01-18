# private  Enkapsulation

class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    def show_saldo(self):
        print(self.__saldo)

data_bank = AkunBank('Bank', 100)
data_bank.show_saldo()