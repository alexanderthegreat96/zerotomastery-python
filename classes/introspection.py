# Introspection in prorgamming
# is the ability to determine the type of an object
# at runetime, ofc
# it's why python is powerful
# as everything in python is an object


# functions to do this

# dir function

from polymorphism import Agent, RogueAgent, Character

agent = Agent()
rogue = RogueAgent()

# will return all the methods 
# and attributes

print(dir(Agent))
print(dir(RogueAgent))

# instanceof

if isinstance(agent, Agent):
    print("Agent is of type Agent")
    
# since it inherits from Character
# it is of type Character as well
    
if isinstance(agent, Character):
    print("Agent is of type Character")