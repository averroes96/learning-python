# for (item in items)
#   // code

nums = range(100)

for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is not even")

## With dictionary

langs = {

    "java" : {
        "experience" : "3 years",
        "progress" : "85%"
    },
    "php" : {
        "experience" : "2 years",
        "progress" : "70%"
    },
    "c" : {
        "experience" : "3 years",
        "progress" : "60%"
    }

}

for lang in langs :
    print(f"Language {lang.capitalize()}\tProgress: {langs[lang].get('progress')}\tExperience: {langs[lang].get('experience')} ")

print("=" * 48)

### Nested for loop

myDict = {
    "averroes": [
        "java",
        "php",
        "c"
    ],
    "epicurus" : [
        "javascript",
        "python"
    ],
    "meceffeuk":[
        "c#",
        "go",
        "c++"
    ]
}

for item in myDict:
    print(f"User: {item.capitalize()}")
    print("Languages:")
    for lang in myDict[item]:
        print(f"> {lang.upper()}")
    print("=" * 48)

### Advanced for dictionary

for key, value in myDict.items():
    print(f"User: {key.capitalize()}")
    print("Languages:")
    for val in value:
        print(f"> {val.upper()}")
    print("=" * 48)