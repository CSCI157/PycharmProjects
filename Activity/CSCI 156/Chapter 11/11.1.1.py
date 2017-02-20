__author__ = 'Fossum'

engineeringdict = dict()
engineeringdict['Alloy'] = 'A mixture of metals or a metal and another element'
engineeringdict['Brittle'] = 'Easily breakable without significant deformation'
engineeringdict['Centripetal Force'] = 'A force that makes a body follow a curved path'
engineeringdict['Drag'] = 'A force acting opposite to the relative motion of any object moving through a fluid'
engineeringdict['Elasticity'] = 'The ability of a body to resist deformation under stress'

print(engineeringdict['Drag'])
print(engineeringdict.get('Alloy'))
print("\n")

for term in engineeringdict:
    print(term)
print("\n")

for i in engineeringdict:
    print(engineeringdict[i])
print("\n")

if engineeringdict.get('Pie') is True:
    print("I like pie")
else:
    print("I want some pie")
