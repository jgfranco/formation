'''
We're going to create a class 'AnimalHouse' with the following functions: 
* addCat() / adoptCat()
* addDog() / adoptDog()
* adoptAnimal()

In this Animal House, cats and dogs are added to the house. When *adoptCat()* or *adoptDog() is called, you return the cat or dog that has been in the house for the longest amount of time. *adoptAnimal()* gets either the cat or dog that has been there the longest.
 
 adoptX() - adopts X animal thats been their the longest
 adoptAnimal() - considers all animals and rtns with the longest time

use a queue structure, separate for each animal
adoptAnimal will consider both, but only remove from one. 

consider when the queue is empty


EXAMPLE(S)
house = AnimalHouse()
house.addCat("Sweet Tea")
house.adoptCat() == "Sweet Tea"
house.addDog("Oliver")
house.addCat("Moose")
house.adoptDog() == "Oliver"
house.adoptDog() == "There are no dogs left to adopt"
house.adoptCat() == "Moose"
house.adoptCat() == "There are no cats left to adopt"
house.adoptAnimal() == "There are no animals left to adopt"
 
CatQ: A0 B1 C2 D3
DogQ: E4

FUNCTION SIGNATURE

# Python
class AnimalHouse:
  def __init__(self):
    # create both queues
    # counter system - integer
    pass

  def addCat(self, cat: str) -> None:
    # append to cat queue
    pass

  def addDog(self, dog: str) -> None:
    # append to dog queue
    pass

  def adoptCat(self) -> str:
    return "There are no cats left to adopt"

  def adoptDog(self) -> str:
    return "There are no dogs left to adopt"

  def adoptAnimal(self) -> str:
    return "There are no animals left to adopt"
'''
from collections import deque

class AnimalHouse:
  def __init__(self):
    # create both queues
    # counter system - integer
    # stores data as a tuple-> (name, int)
    self.dogQ = deque()
    self.catQ = deque()
    self.counter = 0

  def addCat(self, cat: str) -> None:
    # append to cat queue
    self.catQ.append((cat, self.counter))
    self.counter += 1

  def addDog(self, dog: str) -> None:
    # append to dog queue
    self.dogQ.append((dog, self.counter))
    self.counter += 1

  def adoptCat(self) -> str:
    if self.catQ:
        return self.catQ.popleft()[0]

    return "There are no cats left to adopt"

  def adoptDog(self) -> str:
    if self.dogQ:
        return self.dogQ.popleft()[0]

    return "There are no dogs left to adopt"

  def adoptAnimal(self) -> str:
    if self.dogQ and self.catQ:
        if self.dogQ[0][1] < self.catQ[0][1]:
            return self.adoptDog()
        else:
            return self.adoptCat()
    elif self.dogQ:
        return self.adoptDog()
    elif self.catQ:
        return self.adoptCat()
    
    return "There are no animals left to adopt"

# CatQ: A0 B1 C2 D3
# DogQ: E4

# house = AnimalHouse()
# house.addCat("A")
# house.addCat("B")
# house.addCat("C")
# house.addCat("D")
# house.addDog("E")
# print(house.adoptAnimal())
# print(house.adoptAnimal())
# print(house.adoptAnimal())
# print(house.adoptAnimal())
# print(house.adoptAnimal())


house = AnimalHouse()
house.addCat("Sweet Tea")
print(house.adoptCat() == "Sweet Tea")
house.addDog("Oliver")
house.addCat("Moose")
print(house.adoptDog() == "Oliver")
print(house.adoptDog() == "There are no dogs left to adopt")
print(house.adoptCat() == "Moose")
print(house.adoptCat() == "There are no cats left to adopt")
print(house.adoptAnimal() == "There are no animals left to adopt")

rescue = AnimalHouse()
rescue.addCat("Gato")
rescue.addCat("Fato")
rescue.addCat("Napo")
rescue.addCat("Sapo")
rescue.addDog("Barko")
rescue.addDog("Snarpo")
rescue.addDog("Nippo")
rescue.addDog("Paavo")
rescue.addDog("Zozo")
rescue.addCat("Mewo")
print(rescue.adoptCat() == "Gato")
print(rescue.adoptAnimal() == "Fato")
print(rescue.adoptDog() == "Barko")
print(rescue.adoptAnimal() == "Napo")
print(rescue.adoptAnimal() == "Sapo")
print(rescue.adoptAnimal() == "Snarpo")
print(rescue.adoptAnimal() == "Nippo")
print(rescue.adoptDog() == "Paavo")
print(rescue.adoptDog() == "Zozo")
print(rescue.adoptDog() == "There are no dogs left to adopt")
print(rescue.adoptCat() == "Mewo")
print(rescue.adoptAnimal() == "There are no animals left to adopt")
