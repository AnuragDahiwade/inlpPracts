from textblob import Word
word = Word('Eearth')
res = word.correct()
print(res)

word = Word('Battom')
res = word.correct()
print(res)

word = Word('Pappar')
res = word.correct()
print(res)
