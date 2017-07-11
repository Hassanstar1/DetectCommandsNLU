import nltk
from nltk.corpus import treebank
from nltk.grammar import Nonterminal
from nltk import Tree

print("Splitting the Data Set")
# The size of the learning set has to be chosen so that we avoid
# running out of memory when parsing (caused by a too large learned
# grammar). However, a too small size of the learning set, could lead
# to a grammar that is not useful (i.e. it cannot parse sentences
# other than in the learning set).

dataset_size = len(treebank.parsed_sents())
split_size = int(dataset_size * 0.97)

print("Separating Learning Set")
print("Learning set size: " + str(split_size))
learning_set = treebank.parsed_sents()[:split_size]

print("Separating Test Set")
print("Test set size: " + str(dataset_size - split_size))
# This set already contains the parses of the sentences in the test
# set. It is what we are going to compare against, in order to assess
# the quality of the extracted grammar.
test_set = treebank.parsed_sents()[split_size:]

print("Set containing the raw sentences, to be parsed with the extracted grammar")
sents = treebank.sents()
raw_test_set = [[w for w in sents[i]] for i in range(split_size, dataset_size)]

print("Extract the syntactic (and part of the lexical) rules from the learning set")

tbank_productions = []
for sent in learning_set:
    for production in sent.productions():
        tbank_productions.append(production)

print(len(tbank_productions))
print("Extract the rest of the lexical rules from the lexicon")

for word, tag in treebank.tagged_words():
    t = Tree.fromstring("(" + tag + " " + word + ")")
    for production in t.productions():
        tbank_productions.append(production)

print(len(tbank_productions))

print("Creating grammar")
tbank_grammar = nltk.grammar.induce_pcfg(Nonterminal('S'), tbank_productions)

# Uncomment to have a look at the grammar:
# print(tbank_grammar)

print("Initializing parser")

# http://www.nltk.org/_modules/nltk/parse/viterbi.html
parser = nltk.ViterbiParser(tbank_grammar)

# Test the extracted grammar with the Viterbi parser on one sentence.
# The Viterbi parser gives the most probable parse tree
# Test all sentences in the test-set and compare them to the reference parsing

parse_success = 0;
# for i in range(0, len(raw_test_set)):
for i in range(0, 3):
    print("==== Parsing sentence " + str(i), flush=True)  ## Note: flush argument is Python 3
    test_sent = raw_test_set[i]
    # This will raise an exception if the tokens in the test_sentence
    # are not covered by the grammar; should not happen.
    tbank_grammar.check_coverage(test_sent)
    print(test_sent)
    print("[" + str(i) + "] Reference parse:")
    print(test_set[i])
    print("[" + str(i) + "] Parse trees:")
    for tree in parser.parse(test_sent):
        print(tree)
        print(test_sent[i] == tree)
        if test_sent[i] == tree:
            ++parse_success
        print(parse_success)

print("Successfully parsed sentences: " + str(parse_success) + " out of " + str(3))
# print("Successfully parsed sentences: " + str(parse_success) + " out of " + str(len(test_set)))
