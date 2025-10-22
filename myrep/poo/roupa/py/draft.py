class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        if valor == "PP" or "P" or "M" or "G" or "GG" or "XG":
            self.__tamanho = valor 
        else:
            print("Tamanho inválido. Tamanhos permitidos: PP, P, M, G, GG e XG.")
    

def main():
    camisa = Camisa()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "grow":
            camisa(str(arg[1]))
        elif arg[0] == "":
            print(self.__camisa())
        elif arg[0] == "init":
            camisa : camisa = camisa(arg[1])
        elif arg[0] == "show":
            print(camisa)
        else:
           print("Comando nao encontrado")

main()