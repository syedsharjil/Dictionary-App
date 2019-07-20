import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data= json.load(open('Dictionary\data.json'))
def meaning(w1):
    w1=w1.lower()
    if (w1 in data):
        return(data[w1])
    
    elif(w1.upper() in data):
        return(data[w1.upper()]) 
    
    elif(len(get_close_matches(w1,data.keys()))>0):
        print("Did you mean %s ?" %get_close_matches(w1,data.keys())[0])        
        uinp=input("enter Y for yes N for no")
        if(uinp=="Y"):
            return(data[get_close_matches(w1,data.keys())[0]])
        elif(uinp=="N"):
            return("No such word exist")
        else:
            return("We didn't understand your query")
    
    else:
        return("word not found")

w = input("Enter a word")
m=meaning(w)
if(type(m)==list):
    for item in m:
        print(item)
else:
    print("No such word exist")