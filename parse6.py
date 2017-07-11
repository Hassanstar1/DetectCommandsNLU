from nltk import *

grammar1 = CFG.fromstring("""
  S -> PrePolitesse V Contacts Det Intent ADV Telling
  S -> ADV V Contacts Det Intent Telling PrePolitesse
  S -> REP V DestinationP Contacts Det Intent TEM Telling PrePolitesse
  S -> V DestinationP Contacts Det Intent Telling
  S -> V Det Intent DestinationP Contacts Telling PrePolitesse
  S -> V Det Intent Contacts Telling PrePolitesse
  S -> PrePolitesse V Det Intent Contacts Telling
  S -> V Det Intent Contacts Telling
  S -> V Det Intent DestinationP Contacts Telling 
  Telling -> "says:" | ",that_says:" | "that" "says" | "that" "tells" | "that" "tell" | "that" "informs" | "informing"
  PrePolitesse -> "would" "you" "please" | "please" | "would" "you" | "would" "you" "like" | "could" "you" | "I wish" | "I wish you" | "thanks" "to" | "thanks" "for" |
  V -> "send" | "text" | "message" | "sending" | "messaging" | "texting"
  Intent -> "sms" | "message"
  Det -> "a" | "an" | "the" | "my" | "your" | "that" |
  DestinationP -> "to" | "into"
  Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" "Hassan" | "Hassan"
  ADV -> REP TEM | TEM | REP | TEM REP
  REP ->  "daily" | "weekly"|
  TEM -> "at" num "bm" | "at" num "am"| "now" | "at" num |
  num -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
""")

sent = "please send Samer Hassan an sms that says".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

