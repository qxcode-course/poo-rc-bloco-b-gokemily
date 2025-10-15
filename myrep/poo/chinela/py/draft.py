class Chinela:
    def _init_(self):
        self.__tamanho: int = 0

    def _str_(self)->str:
        return f"sua xinela é tamanho: {self.__tamanho}"
    
    def set_tamanho(self, tam: int):
        if tam >= 20 and tam <= 50 and tam %2 == 0:
            self.__tamanho= tam
            return
        print("tamanho inválido")


    def get_tamanho(self):
        return self.__tamanho

def main():
    chinela=Chinela()
    while True:
        n= int(input())
        chinela.set_tamanho(n)
        if chinela.get_tamanho()!=0:
            break

    print(chinela)

main()