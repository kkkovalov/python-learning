class Person:
    def __init__(self, input_name, input_age, input_country):
        self.name = input_name
        self.age = input_age
        self.country = input_country
        self.greeting()
        
    def greeting(self):
        print("Welcome to the club,", self.name)    
        return None
        
    def getAge(self):
        print("Your age is", self.age)
        return None
    

me = Person('Vlad', 20, 'Canada')

me.getAge()
    