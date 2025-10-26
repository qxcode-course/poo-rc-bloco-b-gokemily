class Pessoa:
    def __init__(self, name : str, money: int):
        self.__name = name
        self.__money = money

    def setMoney(self, money: int):
        self.__money = money

    def getMoney(self):
        return self.__money

    def getName(self):
        return self.__name

    def __str__(self):
        return f"{self.getName()}:{self.getMoney()}"

class Motouber:
    def __init__(self):
        self.__cost : int = 0
        self.__driver : Pessoa | None = None
        self.__passenger: Pessoa | None = None 

    def getCost(self) -> int:
        return self.__cost
    def getPassenger(self) -> Pessoa:
        return self.__passenger
    def getDriver(self) -> Pessoa:
        return self.__driver

    def setDriver(self, driver: Pessoa):
        self.__driver = driver
    def setPassenger(self, passenger: Pessoa):
        if self.getDriver() != None:
            self.__passenger = passenger
    def setCost(self, cost: int ):
        self.__cost = cost

    def __str__(self) -> str:
        return f"Cost: {self.getCost()}, Driver: {self.getDriver()}, Passenger: {self.getPassenger()}"

    def LeavePass(self):
        if self.getPassenger == None:
            return 'fail'
        else:
            if self.getPassenger().getMoney() < self.getCost():
                print('fail: Passenger does not have enough money')
                self.getPassenger().setMoney(0)
            else:
                self.getPassenger().setMoney(self.getPassenger().getMoney() - self.getCost())

            self.getDriver().setMoney(self.getDriver().getMoney() + self.getCost())
            self.setCost(0)
            passengerQueSaiu = self.getPassenger()
            self.setPassenger(None)
            return str(passengerQueSaiu) + ' left'

    def Drive(self, distance: int):
        if self.getPassenger() == None and self.getDriver() == None:
            print('fail: empty motorcycle')
        else:
            self.setCost(self.getCost() + distance)



def main():
    motouber = Motouber()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "setDriver":
            motouber.setDriver(Pessoa(arg[1], int(arg[2])))
        elif arg[0] == "setPass":
            motouber.setPassenger(Pessoa(arg[1], int(arg[2])))
        elif arg[0] == "leavePass":
            print(motouber.LeavePass())
        elif arg[0] == "drive":
            motouber.Drive(int(arg[1]))
        elif arg[0] == "show":
            print(motouber)
        elif arg[0] == "init":
            motouber: Motouber = Motouber()
        else:
            print("fail: comando nao existe")

main()