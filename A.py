from nltk import *

grammar1 = CFG.fromstring("""
  S ->  VP NP
  VP -> V NP PP  |  V NP PP NP | V
  PP -> P NP | P NP ADV | ADV P NP | P ADV P NP
  ADV -> REP TEM
  REP -> "each day" | "daily" | "weekly"
  TEM -> "at" num "evening" | "at" num "morning"
  num -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  V -> "call" | "send" | "text"
  NP -> Contacts | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "wife" | "dad" | "husband" | "mam" | "friend" | "sms" | "message"
  P -> "in" | "on" | "by" | "with"| "at" | "to" | "into"
  Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" | "Hassan"
""")
sent = "send an sms to Samer daily at 5 evening".split()
rd_parser = RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

