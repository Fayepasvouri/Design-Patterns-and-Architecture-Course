
# model.py 

class Person(object):
    def __init__(self, name = None, age = None):
        self.name=name
        self.age=age
        
    def name(self):
        return self.name
        
    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
        database = db.mock
        result=[]
        for i in database:
            person=Person(i['name'], i['age'])
            result.append(person)
        return result

# view.py
from model import Person
def showAllView(list): # the list here comes from the previous part where we appended all our results in a list
    print(len(list))
    for i in list:
        print(i.name())
def startView():
    print("Join the club")
def endView():
    print("Goodbye")
    
from model import Person 
import view

def showAll():
   db_people = Person.getAll():
   return view.showAllView(db_people)

def start():
    view.startView():
     input = raw_input()
     if input == 'A':
       return showAll()
     else:
       return view.endView()

if __name__ == "__main__":
   #running controller function
   start()


  # Controller __name__="__main__": interacts with the database and thus with the function that is related to database, here (getAll(self)), and it displays to the end user all the database results fetched there
            
