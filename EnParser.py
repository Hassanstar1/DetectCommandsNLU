import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

# sentences=["tell Ali an sms that says take your medication say it loudly"]#tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]

sentences = ["compose a short message to Samer Hassan and Hassan Loulou say it loudly content take your medication dad",
             "leave a message to dad and say it loudly its content take your medication dad",
             "please send to kameml mahmoud and Samer Hassan a message please say it loudly at 9 pm Tomorrow contains take your medicine",
             "please send sms say it loudly at 9 pm Tomorrow to Hassan body take your medicine",
             "to dad send a message at 10 pm tells take your medication gt3F",
             "give a message for mom say it loudly notify me if answered tell her please, take your medication after 5 mintutes",
             "to dad at 10 pm send a message tells take your medication please it's good for u ;",
             "please send an sms to dad at 9 am repeat everyday  say it loudly  content good morning",
             "for dad send a message content take your medication dad",
             "at 10 pm send a message tells i would like to meet you at your office tommorow morning at 8 pm",
             "i would like sending a message to dad content take your medication dad",
             "leave a message content take your medication dad",
             "give a message to dad content take your medication dad",
             "i want to deliver a message for dad content take your medication dad",
             "to dad at 10:30 pm send a message tells take your medication",
             "to dad send a message at 10 pm  tells call me back",
             "send a message say it in loud voice at 10 pm",
             "please i would like to send a message to Samer Hassan",
             "Could you please send a message that says i would like to meet you at your office tommorow morning at 8 pm",
             "please send to dad content take your medication",
             "please send an sms to dad content take your medication",
             "please send an sms to dad  say it loudly content take your medication",
             "please send an sms to dad at 9 am say it loudly content take your medication",
             "please send an sms to dad at 9 am repeat everyday say it loudly content take your medication",
             "please send an sms at 9 am content good morning",
             "please send an sms to dad at 9 am repeat everyday say it loudly content good morning dad take your medicine"]
"""
            "please send an sms to dad at 9 am repeat everyday say it loudly content good morning ",
            "please send to dad an sms at 9 am repeat everyday say it loudly content good morning ",
            "please send to dad at 9 am repeat everyday  an sms say it loudly content good morning ",
            "please send to dad an sms at 9 am repeat everyday say it loudly content good morning",
            "please send an sms at 9 am to dad repeat everyday say it loudly content good morning ",
            "please send an sms at 9 am repeat everyday to dad say it loudly content good morning",
            "please send an sms at 9 am repeat everyday to dad say it loudly content good morning",
            "please send at 9 am an sms to dad repeat everyday say it loudly content good morning",
            "please send an sms at 9 am to dad repeat everyday say it loudly content good morning",
            "please send an sms to dad repeat everyday at 9 am say it loudly content good morning",
            "please send an sms to dad repeat everyday at 9 am say it loudly content good morning",
            "please send an sms to dad repeat everyday say it loudly at 9 am content good morning",
            "please send an sms repeat everyday to dad at 9 am say it loudly content good morning",
            "please send an sms to dad repeat everyday at 9 am say it loudly content good morning",
            "please send an sms to dad at 9 am repeat everyday  say it loudly content good morning",
            "please send an sms to dad at 9 am say it loudly repeat everyday  content good morning",
            "please send an sms   to dad at 9 am repeat everyday say it loudly content good morning",
            "please send an sms to dad   at 9 am repeat everyday say it loudly content good morning",
            "please send an sms to dad at 9 am repeat everyday say it loudly content good morning",
            "please send an sms to dad at 9 am repeat everyday say it loudly content good morning",
            "please send an sms say it loudly to dad at 9 am repeat everyday content good morning",
            "please send an sms to dad say it loudly at 9 am repeat everyday content good morning",
            "please send an sms to dad at 9 am say it loudly repeat everyday content good morning",
            "please send an sms to dad at 9 am repeat everyday say it loudly content good morning",
            "please send an sms to Samer Hassan and Hassan Loulou at 9 am repeat everyday say it loudly content good morning"]
"""

maverickRecognizerGrammar = CFG.fromstring("""
Command -> CommandSlots | Initial CommandSlots 
CommandSlots -> Slot | Slot CommandSlots | Slot Filler CommandSlots
CommandSlots -> ContentSlot
Slot -> IntentSlot | CommandVerbSlot | TimeSlot | AdditionalSoundSlot | ContactSlot | FrequencySlot | AdditionalNotifySlot
Filler -> TEXT8 | "and" TEXT8
IntentSlot ->  IntentDet Intent | IntentDet Filler Intent | "to" NewVerb IntentDet Intent | "to" NewVerb IntentDet Filler Intent | Intent
IntentDet -> "an" | "a"
NewVerb -> WORD6
Intent -> "sms" | "message"
CommandVerbSlot ->  CommandVerb | "to" CommandVerb 
CommandVerb ->  "send" | "text" | "inform" | "tell" | "texting" | "sending" 
ContentSlot -> ContentInital Content
ContentInital -> "that" "says"  | "tells" | "contains" | "body" | "content"  | "tell" ContentInitalDet | ContentInitalDet  ContentInital
ContentInitalDet -> "him" | "her" | "its" | "the" | "them" 
Content -> TEXT1 
ContactSlot -> "for" Contact | "to" Contact 
ContactSlot -> "for" ContactList | "to" ContactList 
ContactList -> Contact | Contact "and" ContactList
Contact -> TEXT2
TimeSlot ->  "at" Time
Time -> TEXT3
AdditionalSoundSlot -> "say" "it" "loudly" | "say" AdditionalSound | "read" AdditionalSound
AdditionalNotifySlot -> "notify" AdditionalNotify | "notification"
AdditionalSound ->  TEXT4
AdditionalNotify -> TEXT7
FrequencySlot -> "repeat" Frequency
Frequency -> TEXT5 
Initial -> TEXT0
TEXT0 -> WORD0 | WORD0 TEXT0 
TEXT1 -> TEXT 
TEXT ->  WORD | WORD TEXT 
TEXT2 -> WORD2 | WORD2 TEXT2 
TEXT3 -> WORD3 | WORD3 TEXT3 
TEXT4 -> WORD4 | WORD4 TEXT4 
TEXT5 -> WORD5 | WORD5 TEXT5 
TEXT6 -> WORD6 | WORD6 TEXT6 
TEXT7 -> WORD7 | WORD7 TEXT7 
TEXT8 -> WORD8 | WORD8 TEXT8 
""")


def parseToList(s):
    results = None
    results = parse_maverick_command(s)

    return isResultsNotNull(results)


def receiverIsSpecified(tree):
    child_nodes = [child.label() for child in tree
                   if isinstance(child, nltk.Tree)]
    leaves = [subtree.leaves()[0] for subtree in tree.subtrees() if subtree.label() == 'Keyword']
    Receiverleave = [subtree.leaves()[0] for subtree in tree.subtrees() if subtree.label() == 'TEXT2']

    return (('Keyword' in child_nodes) and ('to' in leaves or 'for' in leaves)) or (len(Receiverleave) > 0)


def isResultsNotNull(results):
    i = 0
    for tree in results:
        i += 1
        # print(tree)
        if (i == 1):
            PrintResult(tree)
            # tree.draw()
            if not receiverIsSpecified(tree):
                print("The Receiver is missing in this command")
            else:
                print("The Receiver is available in this command")
        return (i > 0 and i < 2)


def PrintResult(tree):
    for subtree in tree.subtrees():
        if subtree.label() == 'CommandVerb':
            print("CommandVerb = ", subtree.leaves())
        if subtree.label() == 'NewVerb':
            print("CommandVerb = ", subtree.leaves())
        elif subtree.label() == 'Contact':
            print("Receiver = ", subtree.leaves())
        elif subtree.label() == 'Intent':
            print("Intent =", subtree.leaves())
        elif subtree.label() == 'Content':
            print("Content = ", subtree.leaves())
        elif subtree.label() == 'Time':
            print("Time = ", subtree.leaves())
        elif subtree.label() == 'AdditionalSoundSlot':
            print("AdditionalSound = ", subtree.leaves())
        elif subtree.label() == 'AdditionalNotifySlot':
            print("AdditionalNotify = ", subtree.leaves())
        elif subtree.label() == 'FrequencySlot':
            print("Frequency = ", subtree.leaves())
        elif subtree.label() == 'Initial':
            print("Initial = ", subtree.leaves())

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
    words = set(
        [match.group(0) for match in re.finditer(r"[a-zA-Z';.,?:0123456789]+|\.+|\?+|\,+|\!+|\:+|\;+|\'", command)])
    # numbers = set([match.group(0) for match in re.finditer(r"[-+]?\d+[\.+|\:]?\d*", command)])
    # InitialExclusion = ["send","sending", "a", "message", "content", "tells", "deliver", "to"]
    InitialExclusion = ["for", "message", "sms", "send", "sending", "text", "texting", "to", "at", "deliver", "a", "an"]
    ContactExclusion = ["send", "sending", "content", "contains", "message", "tells", "to", "for", "repeat", "say",
                        "notify", "read"
                                  "at", "deliver", "tell", "body", "sms", "a", "an", "and", "notification"]
    VerbExclusion = ["send", "text", "inform", "tell", "texting", "sending"]
    AdditionalNotifyExclusion = ["repeat", "content", "contains", "tells", "to", "for", "at", "say", "tell", "read"]
    AdditionalSoundExclusion = ["at", "repeat", "content", "body", "that", "tells", "to", "for", "at", "notify", "tell",
                                "notification"]
    FrequencyExclusion = ["say", "notify", "content", "contains", "tells", "to", "for", "at", "tell", "body",
                          "notification", "read"]
    TimeExclusion = ["say", "notify", "content", "contains", "tells", "to", "for", "repeat", "send", "notification",
                     "read"]
    FillerExclusion = ["say", "body", "read", "contains", "notify", "a", "an"  "text", "texting", "notification",
                       "content", "tells", "to",
                       "for", "repeat", "send", "message", "sms", "sending", "at", "tell", "deliver", "read"]
    Filler = ["and", "please", ]
    # Make a local copy of productions
    local_maverick_productions = list(maverickRecognizerProductions)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in words])
    # local_maverick_productions.extend([literal_production("NUMBER", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD0", word) for word in words if word not in InitialExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER0", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD2", word) for word in words if word not in ContactExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER2", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD3", word) for word in words if word not in TimeExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER3", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD4", word) for word in words if word not in AdditionalSoundExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER4", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD5", word) for word in words if word not in FrequencyExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER5", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD6", word) for word in words if word not in VerbExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER6", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD7", word) for word in words if word not in AdditionalNotifyExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER7", number) for number in numbers])
    local_maverick_productions.extend(
        [literal_production("WORD8", word) for word in words if word not in FillerExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER7", number) for number in numbers])

    # test  and literal_production("CommandVerb", word) == None

    # Make a local copy of the grammar with extra productions
    local_maverick_grammar = CFG(maverickRecognizerGrammar.start(), local_maverick_productions)

    # Load grammar into a mavericzk_NLU_parser
    maverick_nlu_parser = nltk.RecursiveDescentParser(local_maverick_grammar)

    command_tokens = command.split()

    return maverick_nlu_parser.parse(command_tokens)


true = 0
senNum = 1
for s in sentences:
    print(
        "***************************************************************************************************************************")
    print("Sentence %d" % senNum, "=", s)
    senNum += 1
    # print(s)
    if parseToList(s):
        true += 1
print("Quality=")
print(true / len(sentences))
print("true=", true)
#  if not (parseToList(s) is None)



# run the file on different cases


