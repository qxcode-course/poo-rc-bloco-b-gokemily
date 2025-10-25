class Watch:
    def __init__(self, hora: int, minu: int, seg:int):
        self.__hora = 0
        self.__minu = 0
        self.__seg = 0
        self.setHora(hora)
        self.setMinu(minu)
        self.setSeg(seg)
    
    def setHora(self, hora):
        if hora >= 0 and hora <= 23:
            self.__hora = hora
        else:
           print("fail: hora invalida")

    def setMinu(self, minu):
        if minu >= 0 and minu <= 59:
            self.__minu = minu
        else:
           print("fail: minuto invalido")
    def setSeg(self, seg):
        if seg >= 0 and seg <= 59:
            self.__seg = seg
        else:
           print("fail: segundo invalido")
    
    def getHora(self):
        return self.__hora
    def getMinu(self):
        return self.__minu
    def getSeg(self):
        return self.__seg
    
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.getHora(), self.getMinu(), self.getSeg())
    
    def nextSecond(self):
        if self.getSeg() == 59:
            self.setSeg(0)
            if self.getMinu() == 59:
                self.setMinu(0)
                if self.getHora() == 23:
                    self.setHora(0)
                else:
                    self.__hora += 1
            else:
                self.__minu += 1
        else:
            self.__seg += 1

def main():
    watch = Watch(0,0,0)
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)

        if arg[0] == "end":
            break
        elif arg[0] == "next":
            watch.nextSecond()
        elif arg[0] == "show":
            print(watch)
        elif arg[0] == "set":
            watch.setHora(int(arg[1]))
            watch.setMinu(int(arg[2]))
            watch.setSeg(int(arg[3]))
        elif arg[0] == "init":
            watch: Watch = Watch(int(arg[1]),int(arg[2]),int(arg[3]))
        else:
            print("fail: hora invalida")

main()