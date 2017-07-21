import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree
"""
sentences =["tell dad to take your medication now say it loudly"]
"""
sentences = ["please send an sms daily at 2 pm to Ali body take your medication say it loudly",
             "send an sms to dad at 3 pm content take your medication now say it loudly",
             "tell dad to take your medication now say it loudly",
             "please send an sms to Shadi body please check your email asap say it loudly",
             "send Ahmad a message tells read your speech loudly say it loudly",
             "text Ali at 8 pm tells it is a friendly reminder about our meeting today at 9 pm say it loudly",
             "send Hassan an sms daily at 2 pm body take your medicine say it loudly",
             "tell dad daily at 2 pm to take your medication now say it loudly",
             "send a message to dad tells call me back asap",
             "texting Samer Hassan every Friday at 5 pm tells it is a friendly reminder about our meeting today at 6 pm say it loudly",
             "tell dad everyday this week at 7 am  to take your medication now notify me when it is answered",
             "please send an sms daily this week at 2 pm to Hassan body take your medicine say it loudly"]

maverickRecognizerGrammar = CFG.fromstring("""

Command -> SimpleCommand | ComplexCommand | VariantCommand 

SimpleCommand -> IntentPhrase ContactPhrase BodySentence 
SimpleCommand -> CommandVerb Contacts Intent BodySentence 
SimpleCommand -> CommandVerb Contacts BodySentence 
SimpleCommand -> ContactPhrase IntentPhrase BodySentence 


IntentPhrase -> CommandVerb Inte9nt | CommandVerb
Intent -> "sms" | "an" "sms" | "message" | "a" "message"
CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb

ContactPhrase -> ContactPreposition Contacts
ContactPreposition -> "to" | "for" | "into"
Contacts -> "Shadi" | "Ahmad" | "Ali" | "Samer" "Hassan" | "Hassan" | "dad"

BodySentence -> SMSInitial SMS 
SMSInitial -> "says" | "that" "says" | "tells" | "body" |"content" | "to" | "that" 
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

ComplexCommand -> IntentPhrase ContactPhrase TimePhrase BodySentence 
ComplexCommand -> IntentPhrase Contacts TimePhrase BodySentence 
ComplexCommand -> IntentPhrase TimePhrase ContactPhrase BodySentence 
ComplexCommand -> ContactPhrase IntentPhrase TimePhrase BodySentence
ComplexCommand -> CommandVerb Contacts Intent TimePhrase BodySentence

VariantCommand -> PoliteExpression SimpleCommand | PoliteExpression ComplexCommand
VariantCommand -> SimpleCommand AdditionalCommand | ComplexCommand AdditionalCommand
VariantCommand -> PoliteExpression SimpleCommand AdditionalCommand | PoliteExpression ComplexCommand AdditionalCommand


TimePhrase -> RepeatPhrase TimePreposition Time 
RepeatPhrase -> Repeat TimeDeterminer Range
Repeat -> "repeat" |
TimeDeterminer -> "daily" | "everyday" | "every" Day | 
Day -> "Friday" | "Saturday" | "Sunday" | "Monday" |
Range -> "this" "week" | "this" "month" |
TimePreposition -> "at" 
Time -> TEXT


PoliteExpression -> "please" | "would" "you" "please" | "could" "you" | "I" "would" "like"

AdditionalCommand -> AdditionalCommandInitial AdditionalCommandWhat AdditionalCommandHow
AdditionalCommandInitial -> "say" | "deliver" | "read" | "notify" "me" "when"
AdditionalCommandWhat -> "it" | "the" "content" | "the" "message" | "the" "body" 
AdditionalCommandHow ->   "loudly" | "quietly" | "softly" | "aloud" | "is" "answered" | "is" "delivered"
""")

def parseToList(s):
 results = parse_maverick_command(s)
 if (results is None):
     print("**********************Not parsed***********************")

 i=0
 for tree in results:
    i+=1
    print(tree)

 if (i==0):
   print("====================Not parsed=========================")
 if (i<=1):
   print("=============================================")
 else:
   print("=====================Ambiguity========================")

 return (i>0 and i<2)
 """
    print("=============================================")
    for subtree in tree.subtrees():
        if subtree.label() == 'Intent':
            print("Intent = ", subtree.leaves())
        elif subtree.label() == 'CommandVerb':
            print("CommandVerb = ", subtree.leaves())
        elif subtree.label() == 'Contacts':
            print("Contacts = ", subtree.leaves())
        elif subtree.label() == 'ContactPreposition':
            print("ContactPreposition = ", subtree.leaves())
        elif subtree.label() == 'RepeatPhrase':
            print("RepeatPhrase = ", subtree.leaves())
        elif subtree.label() == 'TimePreposition':
            print("TimePreposition = ", subtree.leaves())
        elif subtree.label() == 'Time':
            print("Time = ", subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            print("SMSInitial = ", subtree.leaves())
        elif subtree.label() == 'SMS':
            print("SMS = ", subtree.leaves())
        elif subtree.label() == 'AdditionalCommand':
            print("AdditionalCommand = ", subtree.leaves())
    print("=============================================")
 """
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
    finalwords = []
    for word in words:
        if not ( word == "say" or word == "notify"):
            finalwords += [word]
    # Make a local copy of productions
    local_maverick_productions = list(maverickRecognizerProductions)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in finalwords])
    local_maverick_productions.extend([literal_production("NUMBER", number) for number in numbers])

    # Make a local copy of the grammar with extra productions
    local_maverick_grammar = CFG(maverickRecognizerGrammar.start(), local_maverick_productions)

    # Load grammar into a mavericzk_NLU_parser
    maverick_nlu_parser = nltk.RecursiveDescentParser(local_maverick_grammar)

    command_tokens = command.split()

    return maverick_nlu_parser.parse(command_tokens)

true =0
for s in sentences:
  print(s)
  if(parseToList(s)):
     true +=1
print("Quality=")
print(true/len(sentences))
#  if not (parseToList(s) is None)



# run the file on different cases



