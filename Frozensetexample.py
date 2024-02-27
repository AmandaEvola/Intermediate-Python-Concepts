# Creating a frozenset
frozen_set = frozenset([1, 2, 3, 4, 4, 5])
print(frozen_set) # Output: frozenset({1, 2, 3, 4, 5})

# Another way to create a frozenset 
another_frozen_set = frozenset({3, 4, 5, 6})

# In Python, a frozenset is an immutable version of a set. It is a built-in data type that represents an unordered collection of unique elements, just like a regular set. However, once a frozenset is created, you cannot modify its elements or add/remove elements. This immutability makes frozensets suitable for situations where you need an unchangeable set.
# Frozensets are particularly useful in scenarios where you need to create sets that remain constant throughout the program's execution, especially in situations where the set is used as a key in dictionaries or an element in other sets.