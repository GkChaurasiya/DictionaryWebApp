import json
import os

if os.path.exists("data.json"):
    data=json.load(open("data.json"))
else:
    print("File not exists!!")
    
def returnMeaning(word):
    if word in data:
        return data[word]
    else:
        return "The Word does not exist. Please double check it."

word=input("Enter word:")

print(returnMeaning(word))

    
        
