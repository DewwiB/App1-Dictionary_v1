import os
import json
from difflib import get_close_matches

def thesaurus(word, file="files/data.json"):
    if os.path.exists(file): #Check file exists
        data = json.load(open(file)) #load data into a variabler
        #print("File found!")
        word = word.lower()#convert to lowercase before checking if it exists
        if word in data: #if the word input is in the dataset, return the word
            return data[word]
        elif word.title() in data: 
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]           
        else:
            #get closest match to user input
            check = get_close_matches(word, data.keys())          
            print("Word not in dictionary.")  
            print("Did you mean: {}".format(check[0]),"?")
            user_confirmation = input("Yes / No: ")
            user_confirmation.lower()

            if user_confirmation == "yes":
                word = check[0]
                return data[word]
            elif user_confirmation =="no":
                return "That word is not in the dictionary,",\
                "Please check it and try again."             
    else:
        word = "quit"
        return "File does not exist, quitting the program..."
        

exit_program = "quit"

while True:
    word = input("Enter a word: ")
    print("-------------------")
    if word == exit_program:
        print("Quitting the program...")
        break
    output = thesaurus(word)
    for item in output:
        print(item)
    print("-------------------")