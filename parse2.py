from nltk import *

grammar1 = CFG.fromstring("""
  S -> V NP Det Intent ADV Telling Told_Activity Activity_Objective TEM
  Telling -> "," Saying 
  Saying -> "says:" | ",that_says:" | "that" "says" | "that" "tells" | "that" "tell" | "that" "informs" | "informing"
  PP -> P NP
  ADV -> REP TEM | TEM | REP |
  REP ->  "daily" | "weekly"|
  TEM -> "at" num "evening" | "at" num "morning"| "now" | "at" num |
  num -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  V -> "send" | "text"
  Told_Activity -> "take" | "close" | "open" | "turn on" | "turn off" | "call"
  Activity_Objective -> Det "medicin" | Det "Car" | Det "Jarden Door"
  Intent -> "sms" | "message"
  NP -> Contacts | Det N | N
  Det -> "a" | "an" | "the" | "my" | "your" | "that"
  N -> "wife" | "dad" | "husband" | "mam" | "friend"
  P -> "in" | "on" | "by" | "with"| "at" | "to" | "into"
  Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" | "Hassan"
""")


sent = "send Shadi a sms daily at 1 evening , says: take a medicin at 1 evening".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

