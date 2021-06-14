'''
Create a arith class.
The class should have a parameterized constructor and methods to add, subtract and multiply two numbers and to return the answers.
'''
class arith:
        def __init__(self,n1,n2):
                self.n1=n1
                self.n2=n2
        
        def add(self):
                print("addition:",self.n1+self.n2)
        def sub(self):
                print("subtraction:",self.n1-self.n2)
        def mul(self):
                print("multiply:",self.n1*self.n2)

n1=int(input("enter the data:"))
n2=int(input("enter the data:"))
obj = arith(n1,n2)
obj.add()
obj.sub()
obj.mul()


