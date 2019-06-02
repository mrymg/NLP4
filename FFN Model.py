import json
import re


def ngram(s, n):
    # Convert to lowercases
    s = s.lower()

    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

mypoem = []

filepath = "unim_poem.json"
with open(filepath, 'r') as dataset:
    file = json.load(dataset)
    for p in file:
        p['poem']= '<start> '+ p['poem'] + ' <end>'

        print(p)