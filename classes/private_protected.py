# private and protected methods

# a private method is a function that can ONLY BE ACCESSED from within the current class
# a protected method is a function that can be accessed only by extending the current class

class Human:
    # constructor is a dunder method
    # it's built into python
    
    def __init__(self, height : float = 6.3, weight : float = 120.0, species : str = "human") -> None:
        self.__height = height
        self.__weight = weight
        self.__species = species

    # private methods
    # beging with their keyword starting with __
    def __what_type(self) -> str:
        return self.__species
    
    def __what_weight(self) -> float:
        return self.__weight
    
    def __what_height(self) -> float:
        return self._what_height
    
    # protected methods
    # being with _ and are accessible only by
    # extending this class
    # this class is going to be a parent or superclass

    def _weight_in(self, unit : str = "kg") -> float:
        unit = "lbs"
        if unit in ["kg", "lbs"]:
            if unit == "kg":
                return self.__what_weight() * 0.453592
            if unit == "lbs":
                return self.__what_weight()
        return 0.00

        
# Mike inherited all the methods from Human
class Mike(Human):
    def __init__(self, height: float = 6.3, weight: float = 120, species: str = "human") -> None:
        # basically initializing Human using the super().__init__()
        super().__init__(height, weight, species)
    
    def mike_weighs(self, unit : str = "kg"):
        return self._weight_in(unit)