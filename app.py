import json
import os
from difflib import get_close_matches

if os.path.exists("data.json"):
    data=json.load(open("data.json"))
else:
    print("File not exists!!")
    
def returnMeaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes or N if No:" % get_close_matches(word,data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The Word does not exist. Please double check it."
        else:
            return "We didn't understand your query."

    else:
        return "The Word does not exist. Please double check it."

word=input("Enter word:")

output=returnMeaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

    
        
