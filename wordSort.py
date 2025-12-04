str = input("Enter a string of words: ")

words = [word.capitalize() for word in str.split()]

words.sort()
print("The sorted words are: ")
for word in words:
    print (word)
    