'''
Create a class cal6 that will calculate area of a square. 
Create setdata() method that should take length from the user.
 Create area() method that will calculate area . 
 Create display() method that will display area .

'''

class cal6:
        def __init__(self,l):
                self.l=l

        def area(self):
                self.area_square=self.l*self.l

        def display(self):
                print("area of a square:",self.area_square)

l = int(input("enter the length of a square:"))
obj = cal6(l)
obj.area()
obj.display()

