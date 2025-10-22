class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        if self.__tamanho == "PP" or "M" or "G" or "GG" or "XG":
            return True #não sei se está certo. Ajeitar depois.
        else:
            print("Tamanho inválido. Tamanhos permitidos: PP, P, M, G, GG e XG.")
    

