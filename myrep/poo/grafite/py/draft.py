class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__size: int = size
        self.__thickness: float = thickness
        self.__hardness: str = hardness

    def getHardness(self) -> int:
        return self.__hardness
    def getSize(self) -> int:
        return self.__size
    def getThickness(self) -> int:
        return self.__thickness

    def setHardness(self, hardness: int):
        self.__hardness = hardness
    def setThickness(self, thickness: int):
        self.__thickness = thickness
    def setSize(self, size: int):
        self.__size = size

    def usagePerSheet(self) -> int:
        if self.getHardness() == "HB":
            return 1
        elif self.getHardness() == "2B":
            return 2
        elif self.getHardness() == "4B":
            return 4
        elif self.getHardness() == "6B":
            return 6

    def __str__(self) -> str:
        return f'[{self.getThickness()}:{self.getHardness()}:{self.getSize()}]'

    
class Pencil:
    def __init__(self, thickness: float):
        self.__tip: Lead = None
        self.__thickness: float = thickness

    def getTip(self) -> Lead:
        return self.__tip
    def getThickness(self):
        return self.__thickness

    def setTip(self, tip: Lead):
        self.__tip = tip
    def setThickness(self, thickness: float):
        self.__thickness = thickness
    
    def hasGrafite(self):
        if self.getTip() == None:
            return False
        else:
            return True

    def insert(self, tip: Lead):
        if self.getTip() != None:
            print('fail: ja existe grafite')
        elif self.getThickness() != tip.getThickness():
            print('fail: calibre incompativel')
        else:
            self.setTip(tip)
        

    def remove(self):
        if self.getTip() != None:
            grafiteRemovido = self.getTip()
            self.setTip(None)
            return grafiteRemovido
        else:
            print('fail: nao existe grafite')
            return None

    def __str__(self) -> str:
        if self.getTip() == None:
            return f'calibre: {self.getThickness()}, grafite: null'
        else:
            return f'calibre: {self.getThickness()}, grafite: {str(self.getTip())}'

    def writePage(self):
        if self.getTip() == None:
            print('fail: nao existe grafite')
        elif self.getTip().getSize() <= 10:
            print('fail: tamanho insuficiente')
        elif self.getTip().usagePerSheet() > self.getTip().getSize() - 10:
            self.getTip().setSize(10)
            print('fail: folha incompleta')
        else:
            self.getTip().setSize(self.getTip().getSize() - self.getTip().usagePerSheet())

def main():
    pencil = Pencil(0.5)
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "insert":
            pencil.insert(Lead(float(arg[1]), arg[2], int(arg[3])))
        elif arg[0] == "remove":
            pencil.remove()
        elif arg[0] == "write":
            pencil.writePage()
        elif arg[0] == "show":
            print(pencil)
        elif arg[0] == "init":
            pencil: Pencil = Pencil(float(arg[1]))
        else:
            print("fail: comando nao existe")

main()