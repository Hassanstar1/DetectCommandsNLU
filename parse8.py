import nltk
from nltk import *
grammar = CFG.fromstring("""
Command -> PrePolitesse CommandVerb Contacts Intent Telling Sentence
PrePolitesse -> "please" | "would" "you" "please" | "could" "you" | "I" "would" "like"
CommandVerb -> "send" | "text" | "sending" | "inform"
Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" "Hassan" | "Hassan"
Intent -> "sms" | "an" "sms" | "message" | "a" "message"
Telling -> "says" | "that" "says" | "tells"
Sentence -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT
""")

productions = grammar.productions()

def literal_production(key, rhs):
    """ Return a production <key> -> n

    :param key: symbol for lhs:
    :param rhs: string literal:
    """
    lhs = Nonterminal(key)
    return Production(lhs, [rhs])

def parse(text):
    """ Parse some text.
"""

    # extract new words and numbers
    words = set([match.group(0) for match in re.finditer(r"[a-zA-Z]+", text)])
    numbers = set([match.group(0) for match in re.finditer(r"\d+", text)])

    # Make a local copy of productions
    lproductions = list(productions)

    # Add a production for every words and number
    lproductions.extend([literal_production("WORD", word) for word in words])
    lproductions.extend([literal_production("NUMBER", number) for number in numbers])

    # Make a local copy of the grammar with extra productions
    lgrammar = CFG(grammar.start(), lproductions)

    # Load grammar into a parser
    parser = nltk.RecursiveDescentParser(lgrammar)

    tokens = text.split()

    return parser.parse(tokens)

results = parse("please send Samer Hassan an sms that says please mom take your medication at 3 pm")
for result in results:
  print (result)


