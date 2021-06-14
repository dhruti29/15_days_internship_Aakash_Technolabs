'''
Consider an employee class, which contains fields such as name and designation.
 And a subclass, which contains a field salary.
 Write a program for inheriting this relation.
'''
class employee:
        def a1(self):
                print("hello :",self.name)
                print("emp destination:",self.des)
class emp(employee):
        def __init__(self,sal,name,des):
                self.sal=sal
                self.name=name
                self.des=des

        def a2(self):
                print("emp salary :",self.sal)

o = emp(100000,"dhruti","QA")
o.a2()
o.a1()