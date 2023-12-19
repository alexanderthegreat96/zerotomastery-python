# MRO -> Method resolution order
# The Method Resolution Order (MRO) in Python defines the order in which base classes
# are searched when looking for a method or attribute in a class hierarchy.
# It is essential to understand MRO, especially in the context of multiple inheritance.

# The C3 linearization algorithm is used to calculate the MRO in Python.
# Here's how it works:

# Depth-First Search (DFS): The MRO is calculated using a depth-first search.
# Starting from the derived class, it traverses the base classes in a depth-first manner.

# Left-to-Right Rule: When there are multiple inheritance paths,
# the leftmost branch is considered first.
# In other words, the base class specified first in the class definition is given higher priority.

class A:
    num = 10

class B(A):
    num = 14

class C(A):
    num = 1


class D(B, C):
    pass

print(D.num) # will print 1 -> as it goes, D -> B -> C -> A
             # the reason why this happens is because B is in front of C and they both inherit from A. 
             # now, if I set num in B to 14, since B is provided before of C, it will return 14, previously,
             # it went through B, but because B wasn't actually modifying anything, that's why it went to C
             