import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree
from nltk.stem.porter import *

maverickRecognizerGrammar = CFG.fromstring("""
Command -> PoliteExpression CommandVerb Intent TimeSentence ContactsSentence BodySentence AdditionalCommand
# Polite request
PoliteExpression -> "please" | "would" "you" "please" | "could" "you" | "I" "would" "like"
# in future can be extended to SendSMSCommandVerbs setAlarmCommandVerbs and soooo
CommandVerb -> "send" | "text" | "sending" | "inform"
# in future will be extended to email
Intent -> "sms" | "an" "sms" | "message" | "a" "message"
# ContactsSentence
ContactsSentence -> ContactPreposition Contacts
#Preposition before contact
ContactPreposition -> "to" | "for" |
# Contacts in future can be extended to more than one contact.
Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" "Hassan" | "Hassan"
# timeSentence to be extended by Ahmad
TimeSentence -> TimePreposition Time
# determine time sentence
TimePreposition -> "at" |
Time -> Number "evening" | Number "morning"| "now" | Number AmPm |
Number -> "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
AmPm -> "am"| "pm"
# BodySentence
BodySentence -> SMSBodyInitial SMSBody | SMSBody
# remove this word from sms body
SMSBodyInitial -> "says" | "that" "says" | "tells" | "body" |"content"|
# sms body
SMSBody -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT
# one or more additional command after sms body to be extended by Ali
AdditionalCommand -> "say" "it" "loudly" | "say" "it" "loudly" AdditionalCommand| "slowly" AdditionalCommand | "and" AdditionalCommand |
""")


def literal_production(key, rhs):
    """ Return a production <key> -> n
    :param key: symbol for lhs:
    :param rhs: string literal:
    """
    lhs = Nonterminal(key)
    return Production(lhs, [rhs])

maverickRecognizerProductions = maverickRecognizerGrammar.productions()


def parse_maverick_command(command):
    """ Parse Maverick Command text."""

    # extract new words and numbers
    words = set([match.group(0) for match in re.finditer(r"[a-zA-Z]+", command)])
    numbers = set([match.group(0) for match in re.finditer(r"\d+", command)])

    # Make a local copy of productions
    local_maverick_productions = list(maverickRecognizerProductions)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in words])
    local_maverick_productions.extend([literal_production("NUMBER", number) for number in numbers])

    # Make a local copy of the grammar with extra productions
    local_maverick_grammar = CFG(maverickRecognizerGrammar.start(), local_maverick_productions)

    # Load grammar into a maverick_NLU_parser
    maverick_nlu_parser = nltk.RecursiveDescentParser(local_maverick_grammar)

    command_tokens = command.split()

    return maverick_nlu_parser.parse(command_tokens)

results = parse_maverick_command("please send sms at 5 pm to Hassan body take your medication say it loudly and slowly")



for result in results:
  print (result)
  result.draw()
