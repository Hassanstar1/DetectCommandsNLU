import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

#sentences=["send an sms to dad content good morning take your medicine"]tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]

#sentences=["send an sms to dad at 9 am July 13 2017 repeat every 4 hours   say it loudly content good morning Dad take your medicine"]

"""@Samer Test"""

sentences =["send an sms to dad at 9 am repeat everyday   say it loudly content good morning take your medicine",
            "send an sms to dad at 9 am repeat everyday    say it loudly content good morning ",
            "send to dad an sms at 9 am repeat everyday   say it loudly content good morning ",
            "send to dad at 9 am repeat everyday  an sms   say it loudly content good morning ",
            "send to dad an sms at 9 am repeat everyday    say it loudly content good morning",
            "send an sms at 9 am to dad repeat everyday    say it loudly content good morning ",
            "send an sms at 9 am repeat everyday  to dad   say it loudly content good morning",
            "send an sms at 9 am repeat everyday   to dad say it loudly content good morning",
            "send at 9 am an sms to dad repeat everyday    say it loudly content good morning",
            "send an sms at 9 am to dad repeat everyday    say it loudly content good morning",
            "send an sms to dad repeat everyday  at 9 am   say it loudly content good morning",
            "send an sms to dad repeat everyday   at 9 am  say it loudly content good morning",
            "send an sms to dad repeat everyday     say it loudly at 9 am content good morning",
            "send an sms repeat everyday to dad at 9 am    say it loudly content good morning",
            "send an sms to dad repeat everyday  at 9 am    say it loudly content good morning",
            "send an sms to dad at 9 am    repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am    say it loudly repeat everyday  content good morning",
            "send an sms   to dad at 9 am repeat everyday  say it loudly content good morning",
            "send an sms to dad   at 9 am repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am   repeat everyday  say it loudly content good morning",
            "send an sms to dad at 9 am repeat everyday  say it loudly  content good morning",
            "send an sms say it loudly to dad at 9 am repeat everyday  content good morning",
            "send an sms to dad say it loudly at 9 am repeat everyday   content good morning",
            "send an sms to dad at 9 am say it loudly repeat everyday   content good morning",
            "send an sms to dad at 9 am repeat everyday  say it loudly  content good morning"]

maverickRecognizerGrammar5 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar4 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar3 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar2 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar1 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT 
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")

def parseToList(s):
 results = None
 for k in range(5,1,-1):
   results = parse_maverick_command(s,k)
   print( results)
   print("*********************Trying to parse the command with grammar number %d"%k)
   if (results is None):
      print("*********************Continue to the next grammar***********************")
   else:
      print("*********************A parsing result is found in grammar number %d"%k)
      break
 print (results)
 if results is None:
      print('====================Not parsed=========================')
      return False
 i=0
 for tree in results:
    i+=1
    #print(tree)

 if (i==0):
   print("====================Not parsed=========================")
 if (i==1):
   print("=============================================")
   PrintResult(tree)
   #tree.draw()
 else:
   print("=====================Ambiguity========================")

 return (i>0 and i<2)

def PrintResult(tree):
    for subtree in tree.subtrees():

        if subtree.label() == 'CommandVerb':
            print("CommandVerb = ", subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            print("Message")
        elif subtree.label() == 'SMS':
            print("", subtree.leaves())
        elif subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'an':
                print("Intent")
            elif subtree.leaves()[0] == 'to':
                print("Receiver")
            elif subtree.leaves()[0] == 'at':
                print("Time")
            elif subtree.leaves()[0] == 'repeat':
                print("Frequency")
            elif subtree.leaves()[0] == 'say':
                print("additional say :")
        elif subtree.label() == 'TEXT1':
            print("", subtree.leaves())

    print("=============================================")

def literal_production(key, rhs):
    """ Return a production <key> -> n

    :param key: symbol for lhs:
    :param rhs: string literal:
    """
    lhs = Nonterminal(key)
    return Production(lhs, [rhs])


maverickRecognizerProductions = maverickRecognizerGrammar5.productions()


def parse_maverick_command(command,i):
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
    if (i==5):
     local_maverick_grammar = CFG(maverickRecognizerGrammar5.start(), local_maverick_productions)
    elif i==4:
     local_maverick_grammar = CFG(maverickRecognizerGrammar4.start(), local_maverick_productions)
    elif i==3:
     local_maverick_grammar = CFG(maverickRecognizerGrammar3.start(), local_maverick_productions)
    elif i==2:
     local_maverick_grammar = CFG(maverickRecognizerGrammar2.start(), local_maverick_productions)
    else:
     local_maverick_grammar = CFG(maverickRecognizerGrammar1.start(), local_maverick_productions)

    # Load grammar into a mavericzk_NLU_parser
    maverick_nlu_parser = nltk.RecursiveDescentParser(local_maverick_grammar)

    command_tokens = command.split()

    return maverick_nlu_parser.parse(command_tokens)

true =0
for s in sentences:
  print("=====================Sentence========================")
  print(s)
  if parseToList(s):
     true +=1
print("Quality=")
print(true/len(sentences))
#  if not (parseToList(s) is None)



# run the file on different cases


