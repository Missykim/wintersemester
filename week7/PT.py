import periodictable 
# Get the symbol and name of the element with atomic number 6 (carbon)
carbon = periodictable.elements[6]
print(carbon.symbol)  # Output: 'C'
print(carbon.name)    # Output: 'carbon'

# Get the mass of an atom of carbon in atomic mass units (amu)
carbon_mass = carbon.mass
print(carbon_mass)    # Output: 12.0107

# Get a list of all the elements in the periodic table
elements = periodictable.elements
print(elements)       # Output: a list of all the elements
