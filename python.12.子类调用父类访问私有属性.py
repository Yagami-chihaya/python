class A :
    def __init__(self):
        self.name="qioayang"
        self.__age=20
    def showAge(self):
        print(self.__age)

class B(A):
    def demo(self):

        
        pass


son = B()

print(son.name)

son.showAge()

