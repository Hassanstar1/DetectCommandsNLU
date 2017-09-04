import nltk
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree

#sentences=["tell Ali an sms that says take your medication say it loudly"]#tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]

sentences =["ارسل رسالة إلى والدي  عند الساعة العاشرة صباحا محتواها كيف حالك يا أبي",
            "يرجى ارسال رسالة إلى أمي كررها كلََ خمس ساعات المحتوى من فضلك يا أمي لا تنسي أخذ الدواء بعد وجبةِ الطعام",
            "أًَريد ارسال رسالة ل سامر حسن تخبره ارجو منك حضور الاجتماع غدا الساعة التاسعة صباحا",
            "أًَريد ارسال رسالة قصيرة ل سمير كامل الساعة الثامنة صباحا اخبره ارجو منك حضور الاجتماع غدا الساعة التاسعة صباحا",
            "أًَريد ارسال رسالة قصيرة لكل من حسن لولو و احمد عبد اللّه الساعة الثامنة صباحا تخبره يرجى حضور الاجتماع غدا الساعة التاسعة صباحا",
            "ابعث إلى سامر حسن رسالة الساعة العاشرة صباحا محتواها كيف حالك يا أبي",
            "اريد أن ابعث رسالة إلى حسن الساعة العاشرة صباحا محتواها كيف حالك يا أبي",
            ]

maverickRecognizerArabicGrammar = CFG.fromstring("""
Command -> CommandSlots | Initial CommandSlots 
CommandSlots -> Slot | Slot CommandSlots
CommandSlots -> ContentSlot
Slot -> IntentSlot | CommandVerbSlot | TimeSlot | AdditionalSoundSlot | ContactSlot | FrequencySlot | AdditionalNotifySlot
IntentSlot ->  Intent | Particle NewVerb Intent
Particle -> "أن" | "ان" 
NewVerb -> WORD6
Intent ->  "رسالة" "نصية" | "رسالة" "قصيرة" | "رسالة"
CommandVerbSlot ->  CommandVerb | Particle CommandVerb 
CommandVerb ->  "ارسل" | "ارسال" | Particle NewVerb
ContentSlot -> ContentInital Content
ContentInital -> "محتواها"  | "تحتوي"  | "اخبره" | "المحتوى"  | "تخبرها" | "تخبره" | "اخبرها" | "بداخلها"
Content -> TEXT1 
ContactSlot -> "ل" ContactList | "إلى" ContactList | "لكل" "من" ContactList | "إلى" "كل" "من" ContactList 
ContactSlot -> Intent ContactList2
ContactList -> Contact | Contact "و" ContactList
ContactList2 -> Contact2 | Contact2 "و" ContactList2
Contact -> TEXT2
Contact2 -> TEXT8
TimeSlot ->  "عند" Time | "الساعة" Time | "في" Time 
Time -> TEXT3
AdditionalSoundSlot -> "انطقها" AdditionalSound
AdditionalNotifySlot -> "ابلغ" AdditionalNotify
AdditionalSound ->  TEXT4
AdditionalNotify -> TEXT7
FrequencySlot -> "كرر" Frequency | "كررها" Frequency
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
        else:
          print("The Receiver is available in this command")
    return (i>0 and i<2)


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
        elif subtree.label() == 'Frequency':
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


maverickRecognizerArabicProductions = maverickRecognizerArabicGrammar.productions()


def parse_maverick_command(command):
    """ Parse Maverick Command text."""

    # extract new arabic words and numbers
    words = set([match.group(0) for match in re.finditer(r"[إّأًٌَُذدٍِجحخهعغفقثصضشسيبلاتنمكطظزوةىرؤءئ';.,?:0123456789]+|\.+|\?+|\,+|\!+|\:+|\;+|\'", command)])
    #numbers = set([match.group(0) for match in re.finditer(r"[-+]?\d+[\.+|\:]?\d*", command)])
    InitialExclusion = [ "رسالة","ارسل", "ارسال", "إلى", "ان", "أن"]
    ContactExclusion = ["send", "رسالة", "المحتوى", "محتواها", "تخبر", "إلى", "ل", "كررها", "تخبره", "عند", "الساعة",  "و"]
    VerbExclusion = ["ارسل", "ارسال"]
    AdditionalNotifyExclusion = ["في", "كرر",]
    AdditionalSoundExclusion = ["عند", "كرر", "محتواها", ]
    FrequencyExclusion = ["محتواها", "المحتوى", "عند"]
    TimeExclusion = ["محتواها", "تخبره", "إلى", "كرر", "اخبره", "اخبرها", "ارسل"]

    # Make a local copy of productions
    local_maverick_productions = list(maverickRecognizerArabicProductions)

    # Add a production for every words and number
    local_maverick_productions.extend([literal_production("WORD", word) for word in words ])
    # local_maverick_productions.extend([literal_production("NUMBER", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD0", word) for word in words if word not in InitialExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER0", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD2", word) for word in words if word not in ContactExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER2", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD3", word) for word in words if word not in TimeExclusion])
    # local_maverick_productions.extend([literal_production("NUMBER3", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD4", word) for word in words if word not in AdditionalSoundExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER4", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD5", word) for word in words if word not in FrequencyExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER5", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD6", word) for word in words if word not in VerbExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER6", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD7", word) for word in words if word not in AdditionalNotifyExclusion])
    #local_maverick_productions.extend([literal_production("NUMBER7", number) for number in numbers])
    local_maverick_productions.extend([literal_production("WORD8", word) for word in words if word not in ContactExclusion])

    # Make a local copy of the grammar with extra productions
    local_maverick_arabic_grammar = CFG(maverickRecognizerArabicGrammar.start(), local_maverick_productions)

    # Load grammar into a mavericzk_NLU_parser
    maverick_AR_nlu_parser = nltk.RecursiveDescentParser(local_maverick_arabic_grammar)

    command_tokens = command.split()

    return maverick_AR_nlu_parser.parse(command_tokens)

true =0
senNum =1
for s in sentences:
  print("***************************************************************************************************************************")
  print("Sentence %d" %senNum,"=",s)
  senNum+=1
  #print(s)
  if parseToList(s):
     true +=1
print("Quality=")
print(true/len(sentences))
#  if not (parseToList(s) is None)



# run the file on different cases


