def myFunction(paraA):
    retVal = 0
    return retVal


class MyClass:
    def __init__(self,x=0,y=0): #self == this
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def myFunction(self,paraA):
        return paraA

    def add(self):
        return self.getX() + self.getY() #self.x + self.y

class MySubClass(MyClass):
    def __int__(self):
        self.z = 0
        self.item_list = []

    def getZ(self):
        return self.z

    def setZ(self,z):
        self.z = z

    def add(self):
        return self.getX() + self.getY()+self.getZ()


def main():
    # code...
    paraA = 0
    retVal = myFunction(paraA)
    myObject = MyClass()
    myObject.setX(5)
    myObject.setY(6)
    retVal = myObject.add()
    print(retVal)

    myNewObject = MyClass(7,8) ##__init__
    mySubObject = MySubClass()

if __name__ == "__main__":
    main()