class Dog:
    
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def descriptor(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
class Bulldog(Dog):
    def __init__(self, name, age):
        self.species = "Bulldog"
        Dog.__init__(self, name, age)

kirk = Dog('Kukla', 4)
koala = Bulldog('Chuka', 2)
print(kirk.descriptor())
print(kirk.speak('Woof woof'))
print(koala.descriptor())