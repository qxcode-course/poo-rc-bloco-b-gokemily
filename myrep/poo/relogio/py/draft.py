class Watch:
    def __init__(self, hora: int, minu: int, seg:int):
        self.setHora(hora)
        self.setMinu(minu)
        self.setSeg(seg)
    
    def setHora(self, hora):
        if hora >= 0 and hora <= 23:
            self.__hora = hora

    def setMinu(self, minu):
        if minu >= 0 and minu <= 59:
            self.__minu = minu

    def setSeg(self, seg):
        if seg >= 0 and seg <= 59:
            self.__seg = seg
    
    def getHora(self):
        return self.__hora
    def getMinu(self):
        return self.__minu
    def getSeg(self):
        return self.__seg
    
    def __str__(self):
        return f"{:02}:{:02}:{:02}".format(self.getHora, self.getMinu, self.getSeg)
    
    def nextSecond(self):
