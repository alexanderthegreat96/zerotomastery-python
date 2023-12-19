# inhetience is the third pillar
# in other words
# allowing inheritence of methods 
# in between classes
# when extending them

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
        # the recomended way of doing it
        super().__init__(level, world_tier, gearscore)
        # we can also call the class directly
        # Character.__init__(self, level, world_tier, gearscore)
        
    def what_dps(self, wp_damage : int = 10) -> float:
        return self._calculate_dps(wp_damage)
    
    # returns agent name
    def whoami(self) -> str:
        return self.__name