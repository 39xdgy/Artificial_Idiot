import spacy

nlp = spacy.load('en_core_web_sm')

example1 = nlp("It This is an example of text tokenization")
'''
for token in example1:
    print(token.text)


from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

example = "Cats Running Was"

example = [stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))
'''

for token in example1:
    print(token.lemma_)
