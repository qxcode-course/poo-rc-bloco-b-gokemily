class Tamagochi:
    def __init__(self, energyMax: int = 100, cleanMax: int = 100):
        self.__energyMax = energyMax
        self.__cleanMax = cleanMax
        self.__energy = energyMax
        self.__clean = cleanMax
        self.__age = 0
        self.__alive = True
        self.setEnergyMax(energyMax)
        self.setCleanMax(cleanMax)
        self.setEnergy(energyMax)
        self.setClean(cleanMax)
        self.setAge(0)
        self.setAlive(True)

    def setEnergyMax(self, energyMax):
        self.__energyMax = energyMax
    
    def setCleanMax(self, cleanMax):
        self.__cleanMax = cleanMax
    
    def setEnergy(self, energy):
        self.__energy = energy
    
    def setClean(self, clean):
        self.__clean = clean
    
    def setAge(self, age):
        self.__age = age

    def setAlive(self, alive):
        self.__alive = alive
    
    def getEnergyMax(self):
        return self.__energyMax
    def getCleanMax(self):
        return self.__cleanMax
    def getEnergy(self):
        return self.__energyMax
    def getClean(self):
        return self.__cleanMax
    def getAge(self):
        return self.__age
    def getAlive(self):
        return self.__alive

class Game:
    def __init__(self, game: Tamagochi):
        self.__bichinho = game
    
    def __str__(self):
        return f"E:{self.__bichinho.getEnergy()}/{self.__bichinho.getEnergyMax()}, L:{self.__bichinho.getClean()}/{self.__bichinho.getCleanMax()}, I:{self.__bichinho.getAge()}"

    def Play(self):
        if self.__bichinho.getAlive() == True and self.__bichinho.getEnergy() <= self.__bichinho.getEnergyMax() and self.__bichinho.getAge() >= 0:
            self.__bichinho.setEnergy(self.__bichinho.getEnergy() -2)
            self.__bichinho.setClean(self.__bichinho.getClean() -3)
            self.__bichinho.setAge(self.__bichinho.getAge() +1)
        else:
            print("fail: pet esta morto")

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


def main():
    game = Tamagochi()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "shower":
            print(game.Shower())
        elif arg[0] == "play":
            print(game.Play())
        elif arg[0] == "sleep":
            print(game.Sleep())
        elif arg[0] == "show":
            print(game)
        elif arg[0] == "set":
            game.setEnergy(int(arg[1]))
            game.setClean(int(arg[2]))
            game.setAge(int(arg[3]))
        elif arg[0] == "init":
            game: Game = Game(Tamagochi(int(arg[1]),int(arg[2])))
        else:
            print("fail: pet esta morto")

main()