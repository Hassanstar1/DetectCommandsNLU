import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

#sentences=["send an sms to dad content good morning take your medicine"]tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]
#sentences=["send an sms to dad at 9 am July 13 2017 repeat every 4 hours   say it loudly content good morning Dad take your medicine"]
sentences =["please send an sms to dad at 9 am repeat everyday  say it loudly  content good morning",
            "to dad send a message content take your medication dad my dad",
            "at 10 pm send a message tells i would like to meet you at your office tommorow morning at 8 pm",
            "i would like sending a message to dad content take your medication dad",
            "leave a message content take your medication dad",
            "give a message to dad content take your medication dad",
            "i want to deliver a message for dad content take your medication dad",
            "to dad at 10 pm send a message tells take your medication",
            "to dad send a message at 10 pm  tells call me back",
            "send a message say it in loud voice at 10 pm",
            "please I would like to send a message to Samer Hassan",
            "Could you please send a message that says i would like to meet you at your office tommorow morning at 8 pm",

            "please send to dad                                    content take your medication",
            "please send an sms to dad                                         content take your medication",
            "please send an sms to dad                           say it loudly content take your medication",
            "please send an sms to dad at 9 am                   say it loudly content take your medication",
            "please send an sms to dad at 9 am  repeat everyday  say it loudly content take your medication",
            "please send an sms at 9 am content good morning",
            "please send an sms to dad at 9 am repeat everyday   say it loudly content good morning dad take your medicine"]
"""
            "please send an sms to dad at 9 am repeat everyday    say it loudly content good morning ",
            "please send to dad an sms at 9 am repeat everyday   say it loudly content good morning ",
            "please send to dad at 9 am repeat everyday  an sms   say it loudly content good morning ",
            "please send to dad an sms at 9 am repeat everyday    say it loudly content good morning",
            "please send an sms at 9 am to dad repeat everyday    say it loudly content good morning ",
            "please send an sms at 9 am repeat everyday  to dad   say it loudly content good morning",
            "please send an sms at 9 am repeat everyday   to dad say it loudly content good morning",
            "please send at 9 am an sms to dad repeat everyday    say it loudly content good morning",
            "please send an sms at 9 am to dad repeat everyday    say it loudly content good morning",
            "please send an sms to dad repeat everyday  at 9 am   say it loudly content good morning",
            "please send an sms to dad repeat everyday   at 9 am  say it loudly content good morning",
            "please send an sms to dad repeat everyday     say it loudly at 9 am content good morning",
            "please send an sms repeat everyday to dad at 9 am    say it loudly content good morning",
            "please send an sms to dad repeat everyday  at 9 am    say it loudly content good morning",
            "please send an sms to dad at 9 am    repeat everyday  say it loudly content good morning",
            "please send an sms to dad at 9 am    say it loudly repeat everyday  content good morning",
            "please send an sms   to dad at 9 am repeat everyday  say it loudly content good morning",
            "please send an sms to dad   at 9 am repeat everyday  say it loudly content good morning",
            "please send an sms to dad at 9 am   repeat everyday  say it loudly content good morning",
            "please send an sms to dad at 9 am repeat everyday  say it loudly  content good morning",
            "please send an sms say it loudly to dad at 9 am repeat everyday  content good morning",
            "please send an sms to dad say it loudly at 9 am repeat everyday   content good morning",
            "please send an sms to dad at 9 am say it loudly repeat everyday   content good morning",
            "please send an sms to dad at 9 am repeat everyday  say it loudly  content good morning"]
"""
maverickRecognizerGrammar6 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar5 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar4 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar3 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
maverickRecognizerGrammar2 = CFG.fromstring("""

Command -> CommandVerb Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a"
SMSInitial -> "that" "says" | "tells" | "body" |"content" | "telling" Determiner "that"
TEXT1 ->TEXT
SMS -> TEXT
TEXT -> WORD | WORD TEXT | NUMBER | NUMBER TEXT

""")
#  Build a new CFG that can accept other variations of commands; sentences begin with the time slot, the contact slot or an initial/polite talk.
maverickRecognizerGrammar1 = CFG.fromstring("""
Command -> CommandSlots ContentSlot | TEXT0 CommandSlots ContentSlot
CommandSlots -> Slot | Slot CommandSlots 
Slot -> Intent | CommandVerb | TimeSlot | AdditionalSlot | ContactSlot | FrequencySlot
Intent ->  "an" "sms" | "a" "message" 
CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent" | "sending"
ContentSlot -> "that" "says" Content | "tells" Content | "body" Content | "content" Content |
Content -> TEXT1 
ContactSlot -> "to" Contact | "for" Contact | "into" Contact
Contact -> TEXT2
TimeSlot ->  "at" Time
Time -> TEXT3
AdditionalSlot -> "say" Additional| "notify" Additional
Additional ->  TEXT4
FrequencySlot -> "repeat" Frequency
Frequency -> TEXT5 
TEXT0 -> WORD0 | WORD0 TEXT0 | NUMBER0 | NUMBER0 TEXT0 
TEXT1 -> TEXT 
TEXT ->  WORD | WORD TEXT | NUMBER | NUMBER TEXT  
TEXT2 -> WORD2 | WORD2 TEXT2 | NUMBER2 | NUMBER2 TEXT2
TEXT3 -> WORD3 | WORD3 TEXT3 | NUMBER3 | NUMBER3 TEXT3
TEXT4 -> WORD4 | WORD4 TEXT4 | NUMBER4 | NUMBER4 TEXT4
TEXT5 -> WORD5 | WORD5 TEXT5 | NUMBER5 | NUMBER5 TEXT5
""")

maverickRecognizerGrammar12 = CFG.fromstring("""
Command -> CommandSlots | TEXT0 CommandSlots
CommandSlots -> Slot | Slot CommandSlots 
Slot -> Intent | CommandVerb | TimeSlot | AdditionalSlot | ContentSlot | ContactSlot | FrequencySlot
Intent ->  "an" "sms" | "a" "message"  
CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent" | "sending"
ContentSlot -> "that" "says" Content | "tells" Content | "body" Content | "content" Content 
Content -> TEXT6
ContactSlot -> "to" Contact | "for" Contact | "into" Contact
Contact -> TEXT2
TimeSlot ->  "at" Time
Time -> TEXT3
AdditionalSlot -> "say" Additional| "notify" Additional
Additional ->  TEXT4
FrequencySlot -> repeat Frequency
Frequency -> TEXT5 

TEXT0 -> WORD0 | WORD0 TEXT0 | NUMBER0 | NUMBER0 TEXT0 
TEXT1 -> TEXT 
TEXT ->  WORD | WORD TEXT | NUMBER | NUMBER TEXT  
TEXT2 -> WORD2 | WORD2 TEXT2 | NUMBER2 | NUMBER2 TEXT2
TEXT3 -> WORD3 | WORD3 TEXT3 | NUMBER3 | NUMBER3 TEXT3
TEXT4 -> WORD4 | WORD4 TEXT4 | NUMBER4 | NUMBER4 TEXT4
TEXT5 -> WORD5 | WORD5 TEXT5 | NUMBER5 | NUMBER5 TEXT5
TEXT6 -> WORD6 | WORD6 TEXT6 | NUMBER6 | NUMBER5 TEXT6
""")



def parseToList(s):
 results = None
 for k in range(6,0,-1):
   print("- Trying to parse the command with grammar number %d"%k)
   results = parse_maverick_command(s,k)
   if not isResultsNotNull(results):
      print("- Continue to the next lower grammar")
   else:
      print("- A parsing result is found in grammar number %d"%k)
      break
 # if isResultsNotNull(results):print('====================Not parsed=========================')
      return False
 return isResultsNotNull(results)

def receiverIsSpecified(tree):
    child_nodes = [child.label() for child in tree
                   if isinstance(child, nltk.Tree)]
    leaves =[subtree.leaves()[0] for subtree in tree.subtrees() if subtree.label() == 'Keyword']
    Receiverleave = [subtree.leaves()[0] for subtree in tree.subtrees() if subtree.label() == 'TEXT2']

    return (('Keyword' in child_nodes) and ('to' in leaves or 'for' in leaves)) or (len(Receiverleave) > 0)
def isResultsNotNull(results):
 i=0
 for tree in results:
    i+=1
    #print(tree)
    if (i == 1):
        PrintResult(tree)
        #tree.draw()
        if not receiverIsSpecified(tree):
          print("The Receiver is missing in this command")
    return (i>0 and i<2)
"""
 if (i==0):
   print("   ====================Not parsed=========================")
 if (i==1):
   print("   =============================================")
   PrintResult(tree)
   #tree.draw()
 else:
   print("   =====================Ambiguity========================")
"""

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
        elif subtree.label() == 'Contact':
            print("Receiver = ", subtree.leaves())
        elif subtree.label() == 'Intent':
            print("Intent =", subtree.leaves())
        elif subtree.label() == 'Content':
            print("Content = ", subtree.leaves())
        elif subtree.label() == 'Time':
            print("Time = ", subtree.leaves())
        elif subtree.label() == 'AdditionalSlot':
            print("Additional = ", subtree.leaves())
        elif subtree.label() == 'FrequencySlot':
            print("Frequency = ", subtree.leaves())


def PrintResult2(tree):

    for subtree in tree.subtrees():

        if subtree.label() == 'CommandVerb':
            print("CommandVerb = ", subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            print("Message")
        elif subtree.label() == 'SMS':
            print("", subtree.leaves())

        if subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'se':
               print("Intent =", subtree.leaves())
            elif subtree.leaves()[0] == 'to':
                print("Receiver", subtree.leaves())
            elif subtree.leaves()[0] == 'at':
                print("Time")
            elif subtree.leaves()[0] == 'repeat':
                print("Frequency")
            elif subtree.leaves()[0] == 'say':
                print("additional say :")
        elif subtree.label() == 'KeywordContent':
            if subtree.leaves()[0] == 'content':
                print("Message = ", subtree.leaves())
        elif subtree.label() == 'TEXT1':
            print("", subtree.leaves())

def literal_production(key, rhs):
    """ Return a production <key> -> n

    :param key: symbol for lhs:
    :param rhs: string literal:
    """
    lhs = Nonterminal(key)
    return Production(lhs, [rhs])


maverickRecognizerProductions6 = maverickRecognizerGrammar6.productions()
maverickRecognizerProductions5 = maverickRecognizerGrammar5.productions()
maverickRecognizerProductions4 = maverickRecognizerGrammar4.productions()
maverickRecognizerProductions3 = maverickRecognizerGrammar3.productions()
maverickRecognizerProductions2 = maverickRecognizerGrammar2.productions()
maverickRecognizerProductions1 = maverickRecognizerGrammar1.productions()

def parse_maverick_command(command,i):
    """ Parse Maverick Command text."""

    # extract new words and numbers
    words = set([match.group(0) for match in re.finditer(r'''(['()""\w.]+|\.+|\?+|\,+|\!+|\:+|\;)''', command)])
    #words = set([match.group(0) for match in re.finditer(r"[a-zA-Z.]+|\.+|\?+|\,+|\!+|\:+|\;", command)])
    numbers = set([match.group(0) for match in re.finditer("[-+]?\d+[\.]?\d*", command)])
    InitialExclusion = ["send","sending", "a", "message", "content", "tells"]
    ContactExclusion = ["send", "sending", "content","a", "message", "tells", "to", "for", "repeat", "say", "notify", "at"]
    AdditionalExclusion = ["at","repeat","content", "tells", "to", "for","at"]
    FrequencyExclusion = ["say","notify","content", "tells", "to","for", "at"]
    TimeExclusion = ["say", "notify", "content", "tells", "to", "for", "repeat"]
    # Make a local copy of productions

    if (i == 6):
     local_maverick_productions = list(maverickRecognizerProductions6)
    elif (i == 5):
     local_maverick_productions = list(maverickRecognizerProductions5)
    elif (i == 4):
     local_maverick_productions = list(maverickRecognizerProductions4)
    elif (i == 3):
     local_maverick_productions = list(maverickRecognizerProductions3)
    elif (i == 2):
     local_maverick_productions = list(maverickRecognizerProductions2)
    elif (i == 1):
     local_maverick_productions = list(maverickRecognizerProductions1)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in words])
    #local_maverick_productions.extend([literal_production("NUMBER", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD0", word) for word in words if word not in InitialExclusion])
    local_maverick_productions.extend([literal_production("NUMBER0", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD2", word) for word in words if word not in ContactExclusion])
    local_maverick_productions.extend([literal_production("NUMBER2", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD3", word) for word in words if word not in TimeExclusion])
    local_maverick_productions.extend([literal_production("NUMBER3", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD4", word) for word in words if word not in AdditionalExclusion])
    local_maverick_productions.extend([literal_production("NUMBER4", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD5", word) for word in words if word not in FrequencyExclusion])
    local_maverick_productions.extend([literal_production("NUMBER5", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD6", word) for word in words])
    local_maverick_productions.extend([literal_production("NUMBER6", number) for number in numbers])

    # Make a local copy of the grammar with extra productions
    if (i==6):
     local_maverick_grammar = CFG(maverickRecognizerGrammar6.start(), local_maverick_productions)
    elif i==5:
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
senNum =1
for s in sentences:
  print("***************************************************************************************************************************")
  print("=====================Sentence %d ========================" %senNum)
  senNum+=1
  print(s)
  if parseToList(s):
     true +=1
print("Quality=")
print(true/len(sentences))
#  if not (parseToList(s) is None)



# run the file on different cases


