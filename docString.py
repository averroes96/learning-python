# DocString is done by the triple ''' ..... '''
# Example:

def sayHello(name):
    '''
    sayHello
        A function that says hello
    Parameters
        name => Name of the person to greet
    '''
    print(f"Welcome {name.lower().capitalize()}")

sayHello("avErrOes")
print(sayHello.__doc__) # Print a function docString