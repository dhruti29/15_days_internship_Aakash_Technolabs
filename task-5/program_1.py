""" 

Create a class cal1 that will calculate sum of three numbers. 
Create setdata() method which has three parameters that contain numbers. 
Create display() method that will calculate sum and display sum.

"""
class calculate:
        def __init__(self,a,b,c):
                self.a= a
                self.b=b
                self.c= c
            
        def display(self):
                print(self.a+self.b+self.c)


obj = calculate(2,3,4)

obj.display()

