# Function recursion

# create a recursive function that removes duplicates in a word

def removeDuplicates(word):

    if(len(word) == 1): # if length = 1 just return the character
        return word
    if(word[0].lower() == word[1].lower()): # if the current and next character are similar remove current char and pass to next
        return(removeDuplicates(word[1:]))

    return word[0] + removeDuplicates(word[1:]) # return the current char and continue recursion


name = removeDuplicates("Aaaaaaaaaaaddddddddddddddddaaaaaaaaaaa")

print(name.capitalize())