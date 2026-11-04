class Animal:
  def __init__(self, name):
    self.name = name

  def feed(self):
    print(self.name,"is eating.")
    
  def make_sound(self):
    print(self.name, "makes a sound")

class Lion(Animal):
  def make_sound(self):
    print(self.name, "roars loudly!")
    print(self.name,"eats fresh meat.")
    
class Elephant(Animal):
  def make_sound(self):
    print(self.name, "trumpets!")
    print(self.name,"eats grass and fruits.")
    
class Monkey(Animal):
  def make_sound(self):
    print(self.name, "chatters!")
    print(self.name,"eats bananas.")
    
animal1 = Animal("Generic Animal")
Lion1 = Lion("Simba")
Elephant1 = Elephant("Dumbo")
Monkey1 = Monkey("George")

print(Lion.make_sound())
print(Lion.feed())
print("-----")

print(Elephant.make_sound())
print(Elephant.feed())
print("-----")

print(Monkey.make_sound())
print(Monkey.feed())
print("-----")


