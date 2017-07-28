import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

#sentences=["tell Ali an sms that says take your medication say it loudly"]#tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]

#sentences=["send an sms at 9 am repeat everyday say it loudly to dad  content good morning"]

"""@Samer Test"""
sentences =["send an sms to dad at 9 am repeat everyday  dad say it loudly content good morning",
            "send an sms to dad at 9 am repeat everyday   dad say it loudly content good morning ",
            "send to dad an sms at 9 am repeat everyday   say it loudly content good morning ",
            "send to dad at 9 am repeat everyday  an sms  dad say it loudly content good morning ",
            "send to dad an sms at 9 am repeat everyday   dad say it loudly content good morning",
            "send an sms at 9 am to dad repeat everyday   dad say it loudly content good morning ",
            "send an sms at 9 am repeat everyday  to dad  dad say it loudly content good morning",
            "send an sms at 9 am repeat everyday  dad to dad say it loudly content good morning",
            "send at 9 am an sms to dad repeat everyday   dad say it loudly content good morning",
            "send an sms at 9 am to dad repeat everyday   dad say it loudly content good morning",
            "send an sms to dad repeat everyday  at 9 am  dad say it loudly content good morning",
            "send an sms to dad repeat everyday   at 9 am dad say it loudly content good morning",
            "send an sms to dad repeat everyday    dad say it loudly at 9 am content good morning",
            "send an sms repeat everyday to dad at 9 am   dad say it loudly content good morning",
            "send an sms to dad repeat everyday  at 9 am   dad say it loudly content good morning",
            "send an sms to dad at 9 am   dad repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am   dad say it loudly repeat everyday  content good morning",
            "send an sms  dad to dad at 9 am repeat everyday  say it loudly content good morning",
            "send an sms to dad  dad at 9 am repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am  dad repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am repeat everyday  say it loudly  content good morning",
            "send an sms say it loudly to dad at 9 am repeat everyday  content good morning",
            "send an sms to dad say it loudly at 9 am repeat everyday   content good morning",
            "send an sms to dad at 9 am say it loudly repeat everyday   content good morning",
            "send an sms to dad at 9 am repeat everyday  say it loudly  content good morning"]

maverickRecognizerGrammar = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT Keyword TEXT Keyword TEXT Keyword TEXT Keyword TEXT SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")

def parseToList(s):
 results = parse_maverick_command(s)
 if (results is None):
     print("**********************Not parsed***********************")

 i=0
 for tree in results:
    i+=1
    #print(tree)

 if (i==0):
   print("====================Not parsed=========================")
 if (i==1):
   print("=============================================")
   print(tree)
 else:
   print("=====================Ambiguity========================")

 return (i>0 and i<2)

def PrintResult(tree):
    for subtree in tree.subtrees():
        if subtree.label() == 'Intent':
            print("Intent = ", subtree.leaves())
        elif subtree.label() == 'CommandVerb':
            print("CommandVerb = ", subtree.leaves())
        elif subtree.label() == 'Contacts':
            print("Contacts = ", subtree.leaves())
        elif subtree.label() == 'ContactPreposition':
            print("ContactPreposition = ", subtree.leaves())
        elif subtree.label() == 'Keyword':
            print("Keyword = ", subtree.leaves())
        elif subtree.label() == 'TEXT':
            print("TEXT = ", subtree.leaves())
        elif subtree.label() == 'Time':
            print("Time = ", subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            print("SMSInitial = ", subtree.leaves())
        elif subtree.label() == 'SMS':
            print("SMS = ", subtree.leaves())
        elif subtree.label() == 'AdditionalCommand':
            print("AdditionalCommand = ", subtree.leaves())
    print("=============================================")

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

    wordsT = words

    finalwords = []
    for word in words:
        if not (word == "say" or word == "notify" or word == "repeat" or word == "at"):
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
  #print(s)
  if(parseToList(s)):
     true +=1
print("Quality=")
print(true/len(sentences))
#  if not (parseToList(s) is None)



# run the file on different cases


