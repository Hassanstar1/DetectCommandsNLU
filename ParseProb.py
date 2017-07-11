import nltk
import _tkinter
from nltk import *
from nltk.tree import *
from nltk.draw import tree

# Grammar creation
grammar = nltk.PCFG.fromstring("""
S -> NP VP 	[1.0]
PP -> P NP 	[1.0]
NP -> Det N 	[0.4]
NP -> Det N PP 	[0.2] 
NP -> 'I' 	[0.4]
VP -> V NP 	[0.5]
VP -> VP PP 	[0.5]
Det -> 'an' 	[0.5] 
Det -> 'my' 	[0.5]
N -> 'elephant' [0.5] 
N ->  'pajamas' [0.5]
V -> 'saw' 	[1.0]
P -> 'in' 	[1.0]
""")

# Import example sentences to NLTK and tokenize them
str_sentence1 = "I saw an elephant"
str_sentence2 = "I saw an elephant in my pajamas"

print("Example sentences")
print(str_sentence1)
print(str_sentence2)
tokens1 = nltk.word_tokenize(str_sentence1)
tokens2 = nltk.word_tokenize(str_sentence2)

# Create the Chart and Viterbi parsers, with the input grammar
chart_parser = nltk.ChartParser(grammar)
viterbi_parser = nltk.ViterbiParser(grammar)

# Results for the Chart Parser
print("Parse trees obtained with the Chart parser")
print("Sentence 1")
for tree in chart_parser.parse(tokens1):
    print(tree)
    tree.draw()

print("Sentence 2")
for tree in chart_parser.parse(tokens2):
    print(tree)
    tree.draw()

# Results for the Viterbi Parser
print("Parse trees obtained with the Viterbi parser")
print("Sentence 1")
for tree in viterbi_parser.parse(tokens1):
    print(tree)
    tree.draw()

print("Sentence 2")
for tree in viterbi_parser.parse(tokens2):
    print(tree)
    tree.draw()
