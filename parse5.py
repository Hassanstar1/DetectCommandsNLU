from nltk import *

grammar1 = CFG.fromstring("""
  S -> PrePolitesse V Contacts Det Intent Telling
  Telling -> "says:" | ",that_says:" | "that" "says" | "that" "tells" | "that" "tell" | "that" "informs" | "informing"
  PP -> DestinationP Contacts
  PrePolitesse -> "would" "you" "please" | "please" | "would" "you" | "would" "you" "like" | "could" "you" | "I wish" | "I wish you" | "thanks" "to" | "thanks" "for" |
  V -> "send" | "text" | "message" | "sending" | "messaging" | "texting"
  Intent -> "sms" | "message"
  Det -> "a" | "an" | "the" | "my" | "your" | "that" |
  DestinationP -> "for"| "at" | "to" | "into"
  Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" | "Hassan"
""")

sent = "please send Ali an sms that says".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

