import re # RegEx module

my_search = re.search(r"[A-Z]", "JavaFX") # Search returns the first occurence

print(my_search.span())
print(my_search.group())

print("=" * 48)

my_search = re.findall(r"[A-Z]", "JavaFX") # Findall returns all the occurences as a list, if empty an empty list

if my_search != False:
    for search in my_search:
        print(search)

print("=" * 48)

my_search = re.split(r"\s", "I hate python") # Split a string according to the given RegEX

print(my_search)

print("=" * 48)

my_search = re.split(r"\s|-|_", "I know_what_it-feels like-to-lose")

for counter, word in enumerate(my_search,1):
    if len(word) == 1:
        continue
    print(f"{counter} => {word.lower()}")


print("=" * 48)

print(re.sub(r"\s", "-", "I know what it feels like to lose", re.IGN)) # Replace a RegEx by a given RegEx in a string

print("=" * 48)


# FLAGS

# re.MULTILINE: check all lines
# re.IGNORECASE: ignore case
# re.DOTALL: Take in consideration new line
# re.VERBOSE: Ignore comments