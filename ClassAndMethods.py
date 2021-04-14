# A9 - COP 1030 - 48320
# Ria Nayar
# Creature Class with 2 objects

class Creature :
  def __init__ (self, name, species, weight) :
    self.name = name
    self.species = species
    self.weight = weight
  def getName (self) :
    return self.name
  def getSpecies (self) :
    return self.species
  def getWeight (self) :
    return self.weight
  def reset (self) :
    self.name = ""
    self.species = ""
    self.weight = 0

creature = Creature("Hope", "Golden Retriever", 65)
name = creature.getName()
species = creature.getSpecies()
weight = creature.getWeight()
print(name, "is a", species, "and weighs", weight, "pounds.")
creature.reset()

creature = Creature("Winter", "Bottlenosed Dolphin", 110)
name = creature.getName()
species = creature.getSpecies()
weight = creature.getWeight()
print(name, "is a", species, "and weighs", weight, "pounds.")
creature.reset()
