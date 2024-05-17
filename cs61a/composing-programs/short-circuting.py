# For AND if all values are true it evaluates to true
# For OR if all values are false it evaluates to false

# Short Circuting refers to pythons ability to evalute booleans from left to right
""" For example"""

print(True or 1/0) # <- This will evaluate to True despite the obvious problem of dividing by 0 because boolean logic short circuts. Because the or statement became True when reading the LHS alone, it evaluated to true before displaying the DIVIDEBYZERO Error 

