import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

"""@Samer Test """
sentences =["send to dad an sms at 9 am repeat everyday content take medication at 12 am go to meet in xx",
            "send an sms to dad at 9 am repeat everyday say it loudly content good morning dad",
            "send an sms to dad at 9 am say it loudly content good morning dad",
            "send an sms to dad at 9 am content good morning dad",
            "send an sms to dad say it loudly content good morning dad",
            "send an sms to dad content good morning dad",
            "send an sms to dad say it loudly at 9 am repeat everyday content good morning dad",
            "send to dad an sms at 9 am repeat everyday content good morning dad",
            "send to dad at 9 am repeat everyday an sms say it loudly content good morning dad",
            "send to dad an sms say it loudly at 9 am repeat everyday content good morning dad",
            "send an sms at 9 am to dad repeat everyday content good morning dad",
            "send an sms at 9 am to dad repeat everyday say it loudly content good morning dad",
            "send an sms at 9 am repeat everyday to dad content good morning dad",
            "send an sms at 9 am repeat everyday say it loudly to dad content good morning dad",
            "send at 9 am an sms to dad repeat everyday content good morning dad",
            "send at 9 am an sms to dad repeat everyday say it loudly content good morning dad",
            "send an sms at 9 am to dad say it loudly repeat everyday content good morning dad",
            "send an sms to dad repeat everyday at 9 am content good morning dad",
            "send an sms to dad repeat everyday at 9 am say it loudly content good morning dad",
            "send an sms to dad repeat everyday say it loudly at 9 am content good morning dad",
            "send an sms to dad at 9 am say it loudly repeat everyday content good morning dad",
            "send an sms repeat everyday to dad at 9 am content good morning dad",
            "send an sms repeat everyday to dad at 9 am say it loudly content good morning dad",
            "send an sms repeat everyday say it loudly to dad at 9 am content good morning dad",
            "send an sms say it loudly repeat everyday to dad at 9 am content good morning dad",
            "send an sms repeat everyday to dad say it loudly at 9 am content good morning dad",
            "send an sms say it loudly to dad repeat everyday at 9 am content good morning dad",
            "send an sms to dad say it loudly repeat everyday at 9 am content good morning dad",
            "send an sms to dad at 9 am repeat everyday say it loudly content good morning dad",
            "send an sms at 9 am repeat everyday to dad say it loudly content good morning dad",
            "send an sms at 9 am say it loudly repeat everyday to dad content good morning dad",
            "send an sms to dad at 9 am repeat everyday content good morning dad",
            "send to dad an sms at 9 am repeat everyday say it loudly content good morning dad",
            "send an sms say it loudly to dad at 9 am repeat everyday content good morning dad"]

maverickRecognizerGrammar = CFG.fromstring("""
Command -> SimpleCommand | ComplexCommand | VariantCommand 

SimpleCommand -> IntentPhrase ContactPhrase BodySentence
SimpleCommand -> CommandVerb ContactPhrase Intent BodySentence 

IntentPhrase -> CommandVerb Intent 
Intent -> "an" "sms" | "a" "message"
CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
ContactPhrase -> ContactPreposition Contacts
ContactPreposition -> "to" | "for" | "into"
Contacts -> TEXT

BodySentence -> SMSInitial SMS 
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
Determiner -> "him" | "her"
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

# Complex Case 1: a command starts with an intent phrase ( i.e a verb + an intent) such as "send an sms"
ComplexCommand -> IntentPhrase ContactPhrase TimePhrase BodySentence 
# Positions and variations for Case 1
ComplexCommand -> IntentPhrase TimePhrase ContactPhrase BodySentence
ComplexCommand -> IntentPhrase AdditionalCommand TimePhrase ContactPhrase BodySentence
ComplexCommand -> IntentPhrase AdditionalCommand ContactPhrase TimePhrase BodySentence
ComplexCommand -> IntentPhrase ContactPhrase AdditionalCommand TimePhrase BodySentence
ComplexCommand -> IntentPhrase ContactPhrase AdditionalCommand BodySentence
ComplexCommand -> IntentPhrase ContactPhrase TimePhrase AdditionalCommand BodySentence
ComplexCommand -> IntentPhrase TimePhrase AdditionalCommand ContactPhrase BodySentence
ComplexCommand -> IntentPhrase TimePhrase ContactPhrase AdditionalCommand BodySentence
ComplexCommand -> IntentPhrase Time ContactPhrase RepeatPhrase BodySentence
ComplexCommand -> IntentPhrase AdditionalCommand Time ContactPhrase RepeatPhrase BodySentence
ComplexCommand -> IntentPhrase Time AdditionalCommand ContactPhrase RepeatPhrase BodySentence
ComplexCommand -> IntentPhrase Time AdditionalCommand RepeatPhrase ContactPhrase BodySentence
ComplexCommand -> IntentPhrase RepeatPhrase AdditionalCommand Time ContactPhrase BodySentence
ComplexCommand -> IntentPhrase Time ContactPhrase AdditionalCommand RepeatPhrase BodySentence
ComplexCommand -> IntentPhrase Time ContactPhrase RepeatPhrase AdditionalCommand BodySentence
ComplexCommand -> IntentPhrase RepeatPhrase ContactPhrase Time BodySentence
ComplexCommand -> IntentPhrase AdditionalCommand RepeatPhrase ContactPhrase Time BodySentence
ComplexCommand -> IntentPhrase RepeatPhrase AdditionalCommand ContactPhrase Time BodySentence
ComplexCommand -> IntentPhrase RepeatPhrase ContactPhrase AdditionalCommand Time BodySentence
ComplexCommand -> IntentPhrase RepeatPhrase ContactPhrase Time AdditionalCommand BodySentence
ComplexCommand -> IntentPhrase ContactPhrase Time AdditionalCommand RepeatPhrase BodySentence
ComplexCommand -> IntentPhrase ContactPhrase RepeatPhrase AdditionalCommand Time BodySentence

# Complex Case 2: a command starts with a verb such as "send" 
ComplexCommand -> CommandVerb ContactPhrase Intent TimePhrase BodySentence

# Positions and variations for Case 2
ComplexCommand -> CommandVerb ContactPhrase Intent TimePhrase AdditionalCommand BodySentence
ComplexCommand -> CommandVerb ContactPhrase Intent Time AdditionalCommand RepeatPhrase BodySentence
ComplexCommand -> CommandVerb ContactPhrase Intent RepeatPhrase AdditionalCommand Time BodySentence
ComplexCommand -> CommandVerb ContactPhrase TimePhrase Intent BodySentence
ComplexCommand -> CommandVerb ContactPhrase Time Intent RepeatPhrase BodySentence
ComplexCommand -> CommandVerb ContactPhrase RepeatPhrase Intent Time BodySentence
ComplexCommand -> CommandVerb TimePhrase Intent ContactPhrase BodySentence
ComplexCommand -> CommandVerb TimePhrase ContactPhrase Intent BodySentence
ComplexCommand -> CommandVerb Time Intent ContactPhrase RepeatPhrase BodySentence
ComplexCommand -> CommandVerb Time Intent ContactPhrase RepeatPhrase AdditionalCommand BodySentence
ComplexCommand -> CommandVerb RepeatPhrase Intent ContactPhrase Time BodySentence
ComplexCommand -> CommandVerb RepeatPhrase Intent ContactPhrase Time AdditionalCommand BodySentence
ComplexCommand -> CommandVerb Time ContactPhrase Intent RepeatPhrase BodySentence
ComplexCommand -> CommandVerb Time ContactPhrase RepeatPhrase Intent BodySentence
ComplexCommand -> CommandVerb RepeatPhrase ContactPhrase Intent Time BodySentence
ComplexCommand -> CommandVerb RepeatPhrase ContactPhrase Time Intent BodySentence
ComplexCommand -> CommandVerb ContactPhrase Intent AdditionalCommand BodySentence
ComplexCommand -> CommandVerb ContactPhrase Intent AdditionalCommand BodySentence
ComplexCommand -> CommandVerb ContactPhrase Intent AdditionalCommand TimePhrase BodySentence
ComplexCommand -> CommandVerb ContactPhrase TimePhrase Intent AdditionalCommand BodySentence

VariantCommand -> PoliteExpression SimpleCommand | PoliteExpression ComplexCommand

TimePhrase -> RepeatPhrase Time | Time RepeatPhrase | Time
RepeatPhrase -> "repeat" TEXT 
Time -> TimePreposition TEXT
TimePreposition -> "at" | "on"


PoliteExpression -> "please" | "would" "you" "please" | "could" "you" | "I" "would" "like" | "I" "wish" "to" 

AdditionalCommand -> AdditionalCommandInitial AdditionalCommandWhat AdditionalCommandHow
AdditionalCommandInitial -> "say" 
AdditionalCommandWhat -> "it" | "the" "content" | "the" "message" | "the" "body" | "this" "message"
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
    print("**********************Structured Model***********************")
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

    # Make a local copy of productions
    local_maverick_productions = list(maverickRecognizerProductions)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in words])
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







