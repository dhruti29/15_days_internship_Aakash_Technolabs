''' 
Create a class cal5 that will calculate area of a rectangle.
 Create constructor method which has two parameters.
 Create calArea() method that will calculate area of a rectangle. 
Create display() method that will display area of a rectangle.
'''

class cal5:
        def __init__(self,l,w):
                self.l=l
                self.w=w
        def calArea(self):
                self.ans = self.l*self.w 
        def display(self):
                print(self.ans)

obj = cal5(6,8)
obj.calArea()
obj.display()
        
