import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data= json.load(open('Dictionary\data.json'))
def meaning(w1):
    w1=w1.lower()
    if (w1 in data):
        return(data[w1])
    else:
        seq=difflib.SequenceMatcher(None, w1,data.keys())
        d=seq.ratio()
        if(d>=0.8)
            return((data.keys()[0)])
        return("word not found")

w = input("Enter a word")
print(meaning(w))
Rain