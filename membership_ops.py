### in and not in

name = "Meceffeuk"
print("e" in name)
print("m" in name) # Case sensitive
print("a" not in name)

langs = [
    "java",
    "php",
    "javascript",
    "python"
]

lang = input("Ask me if i know a certain programming language:\n").strip().lower()

if(lang in langs):
    print(f"Yeah i do speak {lang} :D !")
else:
    print(f"Sorry :( i don't speak {lang} !")