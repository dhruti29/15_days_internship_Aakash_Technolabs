'''
Create a class cal4 that will calculate square of a number. 
Create setdata() method which has one parameters that contain number.
 Create display() method that will calculate sum.(Function should return value)
'''

class cal4:
        def __init__(self,num):
                self.num=num
        def display(self):
                return self.num*self.num


obj = cal4(7)

print(obj.display())
