class Bateria:
    def __init__(self, capacidade):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade
    
    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade
    def getCapacidade(self):
        return self.__capacidade
    
    def setCarga(self, carga):
        self.__carga = carga
    def getCarga(self):
        return self.__carga

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
    
    def setLigado(self, ligado):
        self.__ligado = ligado
    def getLigado(self):
        return self.__ligado
    
    def setBateria(self, bateria):
        self.__bateria = bateria
    def getBateria(self):
        return self.__bateria

    def Usar(self, tempo):
        if self.getLigado() == True:
            self.getBateria().setCarga(self.getBateria().getCarga() - tempo)
            print(f"Usando por {tempo} minutos")
            if self.getBateria().getCarga() == 0:
                self.setLigado(False)
        else:
            print("erro: ligue o notebook primeiro")

    def Ligar(self):
        if self.getLigado() == False and self.getBateria() != None and self.getBateria().getCarga() > 0:
            self.setLigado(True)
            print("notebook ligado")

    def Desligar(self):
        if self.getLigado() == True:
            self.setLigado(False)
            print("notebook desligado")

    def Mostrar(self):
        if self.getLigado() == True:
            print("Status: Ligado")
        else:
            print("Status: Desligado")