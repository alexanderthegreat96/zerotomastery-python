# the final pillar
# polymorphism

# by definition, it's the ability of a type to have another type as well
# it literarelly translates to many-forms
# in OOP it implies that object classes can share the same method name
# but they can act differently based on which object calls them

class Character:
    def __init__(self, level : int = 30, world_tier : int = 3, gearscore : int = 450) -> None:

        # protected methods that we can access using Agent and Rogue Agent
        # because they inherit from Character

        self._level = 40 if level > 40 else level # cap the level to 40
        self._world_tier = 5 if world_tier > 5 else world_tier # cap to 5
        self._gearscore = 500 if gearscore > 500 else gearscore # cap to 500

    # we can calculate the dps for each agent
    def _calculate_dps(self, weapon_damage : int) -> float:
        
        # damage modifiers

        per_level = 1.1
        per_world_tier = 2
        per_gearscore = 0.01

        return (self._level * per_level) + (self._world_tier * 2) + (self._gearscore)

class Agent(Character):

    # class constructor
    # it is calling it's parent / superclass
    # it's not mandatory
    # but the superclass requires some parameter initialization
    # although, not mandatory as we said since the supserclass 
    # has default argument values

    def __init__(self, name: str = "My Agent", level: int = 30, world_tier: int = 3, gearscore: int = 450) -> None:

        # made it private
        # so it cannot be accessed even if extending this class

        self.__name = name
        super().__init__(level, world_tier, gearscore)
    
    # public method accesible when initializing agent
    def what_dps(self, wp_damage : int = 10) -> float:
        # protected method accesible as we inherit from Character
        return self._calculate_dps(wp_damage)
    
    # returns agent name
    def whoami(self) -> str:
        return self.__name
    
class RogueAgent(Character):
    def __init__(self, name : str = "My Rogue Agent", level: int = 30, world_tier: int = 3, gearscore: int = 450) -> None:
        self.__name = name
        super().__init__(level, world_tier, gearscore)

    def what_dps(self, wp_damage : int = 10) -> float:
        return self._calculate_dps(wp_damage)
    
    # returns agent name
    def whoami(self) -> str:
        return self.__name
    


# in here we got 2 different classes that have identical methods
# in this case, whoaimi and what_dps, but they do different things
# method overrides can be done by simply naming the method of the superclass / parent class,
# in our clase Character and giving