dictionary = {
    "Naukar": "Servant",
    "Ghar": "Home",
    "Dost":"Friend",
    "Pyar":"Love"
}
word = (input("Enter the Hindi Word(starting letter is capital): \n")) # Naukar
print(dictionary.get(word,"word not found"))