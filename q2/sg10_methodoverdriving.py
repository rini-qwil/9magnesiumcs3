class Animal: #this is the parent class
  def __init__(self, name): 
    self.name = name

  def feed(self): #this shows the feeding habits of the animals. It is a method that is inherited by the child classes.
    print(self.name,"is eating.")
    
  def make_sound(self): #This shows the sound that the animals make. It is a method that is inherited by the child classes.
    print(self.name, "makes a sound")

class Lion(Animal): #This is the child class that inherits from the parent class Animal. It overrides the make_sound method to provide a specific implementation for lions.
  def make_sound(self):
    print(self.name, "roars loudly!") 
    print(self.name,"eats fresh meat.") #It also overrides the feed method to provide a specific implementation for lions.
    
class Elephant(Animal): #This is the child class that inherits from the parent class Animal. It overrides the make_sound method to provide a specific implementation for elephants.
  def make_sound(self):
    print(self.name, "trumpets!")
    print(self.name,"eats grass and fruits.") #It also overrides the feed method to provide a specific implementation for elephants.
    
class Monkey(Animal): #This is the child class that inherits from the parent class Animal. It overrides the make_sound method to provide a specific implementation for monkeys.
  def make_sound(self):
    print(self.name, "chatters!")
    print(self.name,"eats bananas.") #It also overrides the feed method to provide a specific implementation for monkeys.
    
animal1 = Animal("Generic Animal") #This creates an instance of the Animal class with the name "Generic Animal".
Lion1 = Lion("Simba") #This creates an instance of the Lion class with the name "Simba".
Elephant1 = Elephant("Dumbo") #This creates an instance of the Elephant class with the name "Dumbo".
Monkey1 = Monkey("George") #This creates an instance of the Monkey class with the name "George".

Lion1.make_sound() #This calls the make_sound method of the Lion class, which prints "Simba roars loudly!" and "Simba eats fresh meat."
Lion1.feed()
print("-----") #This prints a separator line for better readability.

Elephant1.make_sound() #This calls the make_sound method of the Elephant class, which prints "Dumbo trumpets!" and "Dumbo eats grass and fruits." 
Elephant1.feed()
print("-----") #This prints a separator line for better readability.

Monkey1.make_sound() #This calls the make_sound method of the Monkey class, which prints "George chatters!" and "George eats bananas."
Monkey1.feed()
print("-----") #This prints a separator line for better readability.


#Made with the help of IntelliSense. (2026, November 4).