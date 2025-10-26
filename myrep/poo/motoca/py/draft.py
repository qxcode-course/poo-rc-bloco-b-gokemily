class Pessoa:
    def __init__(self, name : str, age: int):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def __str__(self):
        return f"{self.getName()}:{self.getAge()}"

class Moto:
    def __init__(self, potencia: int = 1):
        self.__potencia : int = potencia
        self.__time : int = 0
        self.__pessoa: Pessoa | None = None 

    def getPotencia(self) -> int:
        return self.__potencia
    def getTime(self) -> int:
        return self.__time
    def getPessoa(self) -> Pessoa:
        return self.__pessoa

    def setPotencia(self, potencia: int):
        self.__potencia = potencia
    def setTime(self, time: int):
        self.__time = time
    def setPessoa(self, pessoa: Pessoa):
        self.__pessoa = pessoa

    def __str__(self) -> str:
        if self.getPessoa() == None:
            return f"power:{self.getPotencia()}, time:{self.getTime()}, person:(empty)"
        else:
            return f"power:{self.getPotencia()}, time:{self.getTime()}, person:({self.getPessoa()})"

    def Inserir(self, pessoa: Pessoa) -> bool:
        if self.getPessoa() == None:
            self.setPessoa(pessoa)
            return True
        else:
            print('fail: busy motorcycle')
            return False

    def Remover(self) -> Pessoa | None:
        if self.getPessoa() == None:
            return "fail: empty motorcycle"
        else:
            pessoaQueSaiu = self.getPessoa()
            self.setPessoa(None)
            return pessoaQueSaiu

    def BuyTime(self, time: int):
        self.setTime(self.getTime() + time)

    def Drive(self, time: int):
        if self.getTime() == 0:
            print('fail: buy time first')
        elif self.getPessoa() == None:
            print('fail: empty motorcycle')
        elif self.getPessoa().getAge() > 10:
            print('fail: too old to drive')
        elif self.getTime() - time <= 0:
            print(f'fail: time finished after {self.getTime()} minutes')
            self.setTime(0)
        else:
            self.setTime(self.getTime() - time)

    def Honk(self):
        return 'P' + ('e' * self.getPotencia()) + 'm'


def main():
    moto = Moto()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "enter":
            moto.Inserir(Pessoa(arg[1], int(arg[2])))
        elif arg[0] == "leave":
            print(moto.Remover())
        elif arg[0] == "buy":
            moto.BuyTime(int(arg[1]))
        elif arg[0] == "drive":
            moto.Drive(int(arg[1]))
        elif arg[0] == "honk":
            print(moto.Honk())
        elif arg[0] == "show":
            print(moto)
        elif arg[0] == "init":
            moto: Moto = Moto(int(arg[1]))
        else:
            print("fail: comando nao existe")

main()