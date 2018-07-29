import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word does not exist. Please try again."

word = input("Enter word: ")

print(translate(word))

