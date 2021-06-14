'''
Create a class cal2 that will calculate area of a circle.
 Create setdata() method that should take radius from the user. 
 Create area() method that will calculate area . 
Create display() method that will display area .
'''
global pi
pi=3.14
class cla2:
        def __init__(self,r):
                self.r=r
        def area(self):
                self.ans = pi*self.r*self.r
        def display(self):
                print(self.ans)

obj = cla2(4)
obj.area()
obj.display()