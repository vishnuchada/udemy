class Animal(object):
     def __init__(self):
             print "Animal created"
     def whoAmI(self):
             print "Animal"
     def eat(self):
             print "eating"
 
class Dog(Animal):
     def __init__(self):
             Animal.__init__(self)
             print "Dog created"
     def whoAmI(self):
             print "Dog"
     def bark(self):
             print "Woof!"
 
d = Dog()
