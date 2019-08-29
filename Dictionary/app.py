'''

This is a program that loads JSON files and fetch data from the user and give meaning to the user


'''
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("/home/brian/Desktop/Dictionary/data.json"))

def translate(w):
    w.lower()
    match_word = get_close_matches(w, data.keys())[0]
    if word in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        y = input("Did you mean %s instead. Press Y for yes/ N for no? " %match_word)
        #y = input("")
        if y == "y":
            return data[match_word]
        elif y =="n":
            return "You pressed no!!"
        else:
            return "Entered the wrong input"
    else:
        return "The word doesn't exist"

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
