class Subcounter_cl(object):
    def __init__(self, path):
        self.path = path
        self.o = open(self.path + "/data/SUBCOUNT", "r")
        self.maxID = int(self.o.read())
        self.o.close()
    def incr(self):
        self.maxID +=1
        self.o = open(self.path + "/data/SUBCOUNT", "w")
        self.o.write(str(self.maxID))
        self.o.close()
        return int(self.maxID)
    def getmaxID(self):
        return self.maxID    
