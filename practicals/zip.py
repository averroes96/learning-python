## zip() : returns a zip object with the lowest object's length

listOne = [ 1, 2, 3]
listTwo = [ "Java", "PHP", "Python", "C"]
mytuple = ( "85%" , "75%", "70%", "60%")

lists = zip(listOne, listTwo, mytuple)

for item1,item2,item3 in lists:
    print(f"{item1}=>", item2 + " =", item3)