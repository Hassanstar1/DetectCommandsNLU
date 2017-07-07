from nltk import *

grammar1 = CFG.fromstring("""
  S -> TEM V NP Det Intent REP Telling Told_Activity Activity_Objective TEM PrePolitesse | PrePolitesse TEM V NP Det Intent REP Telling Told_Activity Activity_Objective TEM | V NP Det Intent ADV Telling Told_Activity Activity_Objective TEM | REP V NP Det Intent TEM Telling Told_Activity Activity_Objective TEM | V NP Det Intent TEM REP Telling Told_Activity Activity_Objective TEM | ADV V NP Det Intent Telling Told_Activity Activity_Objective TEM | ADV V NP Det Intent Telling Told_Activity Activity_Objective ADV | V NP Det Intent ADV Telling Told_Activity Activity_Objective ADV | V NP ADV Det Intent Telling ADV Told_Activity Activity_Objective | V NP ADV Det Intent Telling Told_Activity ADV Activity_Objective | V NP ADV Det Intent Telling Told_Activity TEM Activity_Objective REP | V NP ADV Det Intent Telling Told_Activity REP Activity_Objective TEM | V NP ADV Det Intent Telling REP Told_Activity Activity_Objective TEM 
  Telling -> "says:" | ",that_says:" | "that" "says" | "that" "tells" | "that" "tell" | "that" "informs" | "informing"
  PP -> DestinationP NP
  PrePolitesse -> "would" "you" "please" | "please" | "would" "you" | "would" "you" "like" | "could" "you" | "I wish" | "I wish you" | "thanks" "to" | "thanks" "for" |
  ADV -> REP TEM | TEM | REP | TEM REP
  REP ->  "daily" | "weekly"|
  TEM -> "at" num "bm" | "at" num "am"| "now" | "at" num |
  num -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  V -> "send" | "text" | "message" | "sending" | "messaging" | "texting"
  Told_Activity -> "take" | "close" | "open" | "turn on" | "turn off" | "call"
  Activity_Objective -> Det "medicin" | Det "Car" | Det "Jarden Door"
  Intent -> "sms" | "message"
  NP -> Contacts | Det N | N | DestinationP NP |DestinationP Det N
  Det -> "a" | "an" | "the" | "my" | "your" | "that"
  N -> "wife" | "dad" | "husband" | "mam" | "friend"
  DestinationP -> "for"| "at" | "to" | "into"
  Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" | "Hassan"
""")


sent = "would you please at 1 bm send to my dad an sms daily that says take your medicin at 2 bm".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

