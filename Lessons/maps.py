#map, takes in two parameters(function,data)
from random import shuffle

words=['beetroot','carroots','potatoes']
anagrams=[]

def jumble(word):
    anagram=list(word)
    shuffle(anagram)
    return ''.join(anagram)
  
jumble(word='mercy')

print(list(map(jumble,words))) #map method

print([jumble(word) for word in words]) #comprehension

for word in words: #FOR IN LOOP
    anagrams.append(jumble(word))
print(anagrams)

