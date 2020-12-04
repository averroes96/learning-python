# while condition :

a = 0

while a < 10:
    print(f"a = {a}")
    a += 1

print("=" * 48)

# while training

friends = [
    "Faysal", 
    "Idris",
    "Karim",
    "Walid",
    "Oussama"
]

cpt = 0

while(cpt < len(friends)):

    print(f"Friend #{str(cpt+1).zfill(2)}:\t{friends[cpt]}")
    cpt += 1
else:
    print("=" * 48)

### While practice

favWebs = []
maxWebs = 5

while( maxWebs > 0 ):
    newWeb = input("Enter Website name: \thttps://").strip().lower()
    favWebs.append(f"https://{newWeb}")
    maxWebs -= 1
    print(f"{newWeb} added, {maxWebs} left !")
    print(favWebs)
else:
    print("Can't add anymore websites ! bookmark full")

index = 0

while(index < len(favWebs)):
    print(f"Website #{(index+1)}:\t{favWebs[index]}")
    index += 1