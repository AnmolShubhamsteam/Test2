import numpy as np 
class Calcuator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.b-self.a
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def log(self):
        return np.log(self.a)
    def sin(self):
        return np.sin(self.a)
    def cos(self):
        return np.cos(self.a)
    def tan(self):
        return np.tan(self.a)


if __name__=="__main__":
    a=Calcuator(20,30)
    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())
    print(a.log())
    print(a.sin())
    print(a.cos())
    print(a.tan())
