class person:
    def __init__(self, name, age) :
        self.name= name
        self.age= age
person1 =person("Alice", 30)
class dog :
    def __init__(self, name) :
      self.name=name
    def bark(self):
        return f"{self.name} says woof!"
dog1= dog("buddy")
print(dog1.bark())
class Animal:
    def speak(self):
        raise NotImplementedError("subclass must implement abstract method")
class dog(Animal):
    def speak(self):
        return 'Woof!'