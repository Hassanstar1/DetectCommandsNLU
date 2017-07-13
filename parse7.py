from nltk import *

grammar1 = CFG.fromstring("""
Command -> PrePolitesse CommandVerb Contacts Intent Telling Sentence
PrePolitesse -> "please" | "would" "you" "please" | "could" "you" | "I" "would" "like"
CommandVerb -> "send" | "text" | "sending" | "inform"
Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" "Hassan" | "Hassan"
Intent -> "sms" | "an" "sms" | "message" | "a" "message"
Telling -> "says" | "that" "says" | "tells"
Sentence -> NounPhrase VerbPhrase | VerbPhrase NounPhrase 
NounPhrase -> Noun | Determiner Noun | Determiner Noun PrepositionalPhrase| Noun PrepositionalPhrase
VerbPhrase -> Verb | Verb Determiner | Verb NounPhrase | Verb Determiner NounPhrase
VerbPhrase -> Verb NounPhrase PrepositionalPhrase 
Noun -> "medication" | "hospital" | "doctor" | "I" | "Wife" | "Dad" | "You" | "mom" | "message" 
Determiner -> "a" | "the" | "your" | "my" | "me" 
Verb -> "take" | "go" | "buy" | "visit" | "call" | "send"
Preposition -> "to" | "for" | "about" | "with" | "at"
""")

sent = "please send Samer Hassan an sms tells take your medication".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)


sent = "please send Samer Hassan an sms that says visit your doctor at hospital".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = "please send Samer Hassan an sms that says send me a message".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)