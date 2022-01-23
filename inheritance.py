class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
class Monkey(Animal):
    pass

x = Animal("Pete the Cat")
y = Monkey("George")

print(x, type(x))
print(y, type(y))

x.say_hi()