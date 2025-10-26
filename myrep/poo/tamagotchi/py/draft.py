class Tamagochi:
    def __init__(self, energyMax: int = 100, cleanMax: int = 100, energy: int = 100, clean: int = 100, age: int = 0, alive: bool = True):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy = energy
        self.__clean = clean
        self.__age = age
        self.__alive = alive
        self.setEnergyMax(energyMax)
        self.setCleanMax(cleanMax)
        self.setEnergy(energy)
        self.setClean(clean)
        self.setAge(age)
        self.setAlive(alive)

    def setEnergyMax(self, energyMax):
        if energyMax >= 1:
            self.__energyMax = energyMax
    
    def setCleanMax(self, cleanMax):
        if cleanMax >= 1:
            self.__cleanMax = cleanMax
    
    def setEnergy(self, energy):
        if energy >= 1 and energy < energyMax:
            self.__energy += 1
        else:
            print("fail: pet esta morto")
    
    def setClean(self, clean):
        if clean >= 1 and clean < cleanMax:
            self.__energy += 1
        else:
            print("fail: pet morreu de sujeira")
    
    def setAge(self, age):
        if age >= 1:
            self.__age += 1
        else:
            print("fail: pet esta morto")

    def setAlive(self, alive):
        if alive == True:
            self.__alive = alive
        else:
            print("fail: pet esta morto")
    
    def getEnergyMax(self):
        return self.__energyMax
    def getCleanMax(self):
        return self.__cleanMax
    def getEnergy(self):
        return self.__energy
    def getClean(self):
        return self.__clean
    def getAge(self):
        return self.__age
    def getAlive(self):
        return self.__alive

class Game:
    def __init__(self, tamagochi: Tamagochi):
        self.__bichinho = tamagochi
    
    def __str__(self):
        return f"E:{self.__bichinho.getEnergy()}/{self.__bichinho.getEnergyMax()}, L:{self.__bichinho.getClean()}/{self.__bichinho.getCleanMax()}, I:{self.__bichinho.getAge()}"

    def Play(self):
        if self.__bichinho.alive == True:
            

    

    def Shower(self):
        if self.__bichinho.alive == True:
            self.bichinho.setClean(self.bichinho.getCleanMax())
        else:
            print("fail: pet esta morto")

    def Sleep(self):
        if self.__bichinho.energy <= self.__bichinho.energyMax and self.__bichinho.energy > 0 and self.__bichinho.alive == True:
            self.bichinho.setEnergy(self.bichinho.getEnergyMax())
        else:
            print("fail: pet esta morto")