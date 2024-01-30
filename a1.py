class Calcuator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b


if __name__=="__main__":
    a=Calcuator(20,30)
    print(a.add())