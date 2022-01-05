# Add implementation method
def add(x,y):
    return x + y

# Subtract implementation method
def subtract(x,y):
    return x - y    #on master branch

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