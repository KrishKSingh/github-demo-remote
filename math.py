# Add implementation method
def add(x,y):
    return x + y    #on Bug123 branch

# Subtract implementation method
def subtract(x,y):
    return x - y    #from remote repo

# Multiply implementation method
def multiply(x,y):
    return x * y    # on Bug456 branch

# Divide implementation method
def divide(x,y):
    if y == 0:      # on master branch	
        return DIVIDE_BY_0_ERROR
    else:
        return x / y
        
# Square Implentation method
def square(x):
    return x * x
