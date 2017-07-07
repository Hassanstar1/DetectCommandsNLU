from nltk.parse.generate import generate
from nltk import CFG

grammar1 = CFG.fromstring("""
  S -> V NP ADV
  PP -> P NP 
  ADV -> REP TEM 
  REP -> "each day" | "daily" | "weekly"
  TEM -> "at" num "evening" | "at" num "morning"
  num -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
  V ->  "send" Comp| "text" Comp
  Comp -> "sms" to NP | "message" to NP
  NP -> "Shadi" | "Ahmad" | "Ali" | "Samer" | "Hassan" | Det N
  Det -> "a" | "an" | "the" | "my"
  N -> "wife" | "dad" | "husband" | "mam" | "friend" 
  P -> "in" | "on" | "by" | "with"| "at" | "to" | "into"
  """)

for sentence in generate(grammar1, n=1000):
   print(' '.join(sentence))