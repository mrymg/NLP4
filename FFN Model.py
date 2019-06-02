import json
import re
# import dynet as dy

###################################################################
###################################################################
# We're getting file and make bigram and create uniquelists.
###################################################################
###################################################################


def ngram(s, n):
    # Convert to lowercases
    s = s.lower()

    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^\a-zA-Z0-9\s]', ' ', s)

    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

mypoem = []
myBigram=[]
filepath = "unim_poem.json"
with open(filepath, 'r') as dataset:
    file = json.load(dataset)[:5000]
    for p in file:
        p['poem']= '<start> '+ p['poem'] + ' <end>'
        p['poem']= str(p['poem']).replace("\n"," *n ")
        myBigram += ngram(str(p['poem']), 2)

cogul=[]
for i in myBigram:
   cogul.append(i.split(' ')[0])
   cogul.append(i.split(' ')[1])

tekil= list(set(cogul))
print(len(tekil))
###################################################################
###################################################################
####        Creating the one-hot vector.



