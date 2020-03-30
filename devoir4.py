#coding: utf-8

import csv, spacy
from collections import Counter


nlp = spacy.load("fr_core_news_md")

martino = "martino.csv"
chronique = open(martino)
# print(chronique)
chronique = csv.reader(chronique)
# print(chronique)
next(chronique)
# print(chronique)

# for row in chronique:         <-- test
#     print(row)

tousMots = []
bigrams = []
ls = []

for row in chronique:
    # print(row[3])
    doc = nlp(row[3])
    tokens = [token.text for token in doc]
    # print(tokens)
    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    for lemme in lemmes:
        tousMots.append(lemme)
    
    for x, y in enumerate (lemmes[:-1]):
        bigrams.append("{} {}".format(lemmes[x], lemmes[x+1]))
for bigram in bigrams:
    if "islam" in str(bigram):
        ls.append(bigram)
    elif "musul" in str(bigram):
        ls.append(bigram)
list = Counter(ls)
print(list.most_common(50))
