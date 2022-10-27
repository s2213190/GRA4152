class Person:
    def __init__(self,name,year_of_birth):
        self._name= name
        self._yob = year_of_birth 
        
    def __repr__(self):
        return "This is a Superclass called Person"

class Student(Person):
    def __init__(self, name, year_of_birth, major):
        super().__init__(name, year_of_birth)
        self._major = major
    
    def __repr__(self):
        return "This is a Subclass called Student"

class Instructor(Person):
    def __init__(self, name, year_of_birth, salary):
        super().__init__(name, year_of_birth)
        self._salary = salary
    
    def __repr__(self):
        return "This is a Subclass called Instructor"
        

John = Person("Pratik", 2012)
Sam = Student("Sam", 2000, "MBA")
Doris = Instructor("Doris", 2000, 50000)

print(John)
print(Sam)
print(Doris)