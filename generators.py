# Generator => Function with "yield" keyword instead of return

def myGen():
    yield "C"
    yield "Java"
    yield "PHP"
    yield "Python"

print(myGen)

# Generators supports iterators

gens = myGen()

print(next(gens))
print(next(gens))

for gen in gens:
    print(gen)