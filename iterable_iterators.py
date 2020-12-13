## Iterable = [String, tuple, list, dict, set]

langs = ["Java", "Python", "PHP", "C"]

for lang in langs:
    print(lang)

print("=" * 48)

name = "Meceffeuk"

for letter in name:
    print(letter, end="-")

print("\n")
## Iterator: iter(langs) | iter by next()

iterator = iter(langs)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) : StopIteration