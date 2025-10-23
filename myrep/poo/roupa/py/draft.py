class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def __str__(self):
        return f"size: ({self.__tamanho})"

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor 
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")    

def main():
    camisa = Camisa()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "size":
            camisa.setTamanho(str(arg[1]))
        elif arg[0] == "":
            print(camisa)
        elif arg[0] == "init":
            camisa : camisa = camisa(arg[1])
        elif arg[0] == "show":
            print(camisa)
        else:
           print("Comando nao encontrado")

main()