from nltk.corpus import wordnet

antonyms = []
text = "north south up down love"
x = text.split(" ")

for k in x:
    for syn in wordnet.synsets(k):
        for i in syn.lemmas():
            if i.antonyms():
                antonyms.append(i.antonyms()[0].name())

print(set(antonyms))