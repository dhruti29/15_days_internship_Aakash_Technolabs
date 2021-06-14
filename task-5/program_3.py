'''
Create a class cal3 that will calculate simple interest.
 Create constructor method which has three parameters .
 Create calInterest() method that will calculate Interest . 
Create display() method that will display Interest.
'''
class cal3:
        def __init__(self,p,r,t):
                self.p=p
                self.r=r 
                self.t=t
        def calInterst(self):
                self.ans = (self.p*self.r*self.t)/100
        def dispaly(self):
                print(f"interst is {self.ans}")
obj = cal3(10000,10,365)
obj.calInterst()
obj.dispaly()

        