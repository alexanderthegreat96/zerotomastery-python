from classes import PlayerCharacter
from private_protected import Mike
from inheritence import RogueAgent, Agent

# normal class initialization
player = PlayerCharacter("Mike", 28)
player.shout()

# initializing the class through the classmethod
# that initializes the class
new_class = PlayerCharacter.build_class("alex", 29)
new_class.shout()

# initializing 
static = PlayerCharacter.modify_this(18)
print(static)

# abstraction

mike = Mike()
print(mike.mike_weighs())

# inheritence +  abstraction
# this showcases polymorphism too
# as Agent is of type Agent but it is also of type Character
# as RogueAgent is of type RogueAgent but it is also of type Character
# since it initializes it
# and inherits whatever protected / public properties it has

agent = Agent("Michael", 34, 4, 430)
print("This is agent: " + agent.whoami())
print(agent.what_dps(36000))

rogue = RogueAgent("Bonafide", 40, 5, 500)
print("This is rogue agent: " + rogue.whoami())
print(rogue.what_dps(41222))