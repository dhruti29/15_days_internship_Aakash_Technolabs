'''
Write a program with use of inheritance: 
Define a class publisher that stores the name of the title. 
Derive two classes book and tape, which inherit publisher. 
Book class contains member data called page no and tape class contain time for playing.
Define functions in the appropriate classes to get and print the details.
'''
class publisher:
        def display(self):
                print("page no:", self.page)
                print("time for playing:",self.play)

class book(publisher):
        def book_info(self,page):
                self.page=page


class tape(publisher):
        def publisher_info(self,play):
                self.play=play

obj1= book()

obj1.book_info(100)
obj2= tape()

obj2.publisher_info("10:00 am")
obj2.display()
obj1.display()




