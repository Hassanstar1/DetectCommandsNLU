import nltk
import sys
from tkinter import *
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree
from tkinter import *
import speech_recognition as sr



#sentences=["send an sms to dad content good morning take your medicine"]tell Ali the following message xxxx", "text Ali with the following sms xxx", "send an sms that contains the content xxx to Ali"]
#sentences=["send an sms to dad at 9 am July 13 2017 repeat every 4 hours   say it loudly content good morning Dad take your medicine"]
# send an sms to dad at 5 pm everyday content xxx
"""
sentences =["send        to dad                                         content take your medication",
            "send an sms to dad                                         content take your medication",
            "send an sms to dad                           say it loudly content take your medication",
            "send an sms to dad at 9 am                   say it loudly content take your medication",
            "send an sms to dad at 9 am  repeat everyday  say it loudly content take your medication",
            "send an sms to dad at 9 am repeat everyday   say it loudly content good morning take your medicine"]

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
"""
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
 for k in range(5,0,-1):
   #print("- Trying to parse the command with grammar number %d"%k)
   results = parse_maverick_command(s,k)
   if  isResultsNotNull(results):
      break
 return isResultsNotNull(results)

def parseToList2(s):
 ParsedWellv,whichk = ParsedWell(s)
 if ParsedWellv:
  return resToString(s,whichk)


def resToString(s,k):
    global tt
    parse_string = ''
    results = parse_maverick_command(s, k)
    for tree in results:
        parse_string += ' '.join(str(PrintResult2(tree)))
        tt=tree
    return parse_string,tt

def PrintResult2(tree):
    #drawing(tree)
    global ctree
    ctree=''
    for subtree in tree.subtrees():
        if subtree.label() == 'CommandVerb':
            ctree+= ('CommandVerb = ')
            ctree+=str(subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            ctree +='\n Message'
        elif subtree.label() == 'SMS':
            ctree +=''
            ctree +=str(subtree.leaves())
        elif subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'an':
                ctree +='\n Intent'
            elif subtree.leaves()[0] == 'to':
                ctree +='\n Receiver'
            elif subtree.leaves()[0] == 'at':
                ctree +='\n Time'
            elif subtree.leaves()[0] == 'repeat':
                ctree +='\n Frequency'
            elif subtree.leaves()[0] == 'say':
                ctree +='\n additional say :'
        elif subtree.label() == 'TEXT1':
            ctree +=''
            ctree +=str(subtree.leaves())
    return ctree

def ParsedWell(s):
 solvedBy=-1
 istrue=False
 results = None
 for k in range(5,0,-1):
   print("- Trying to parse the command with grammar number %d"%k)
   results = parse_maverick_command(s,k)
   if  isResultsNotNull(results):
       istrue= True
       solvedBy=k
       break
   else:
       print("It wassssssssssss Falssssssssssssssssssssssssssssssssssssssssssssse")
       isture= False
 return istrue,solvedBy

def isResultsNotNull(results):
 i=0
 for tree in results:
    i+=1
 return (i>0 and i<2)

def literal_production(key, rhs):
    """ Return a production <key> -> n

    :param key: symbol for lhs:
    :param rhs: string literal:
    """
    lhs = Nonterminal(key)
    return Production(lhs, [rhs])

def product():
    global maverickRecognizerProductions5
    maverickRecognizerProductions5 = maverickRecognizerGrammar5.productions()
    global maverickRecognizerProductions4
    maverickRecognizerProductions4= maverickRecognizerGrammar4.productions()
    global maverickRecognizerProductions3
    maverickRecognizerProductions3= maverickRecognizerGrammar3.productions()
    global maverickRecognizerProductions2
    maverickRecognizerProductions2= maverickRecognizerGrammar2.productions()
    global maverickRecognizerProductions1
    maverickRecognizerProductions1= maverickRecognizerGrammar1.productions()

def parse_maverick_command(command,i):
    """ Parse Maverick Command text."""

    # extract new words and numbers
    words = set([match.group(0) for match in re.finditer(r"[a-zA-Z]+", command)])
    numbers = set([match.group(0) for match in re.finditer(r"\d+", command)])
    # Make a local copy of productions

    if (i == 5):
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

def parse(sentences):
    global parsingResult
    parsingResult='Result is : \n'
    true =0
    senNum =1
    for s in sentences:
      print("***************************************************************************************************************************")
      print("=====================Sentence %d ========================" %senNum)
      senNum+=1
      print(s)
      istrue, solvedby = ParsedWell(s)
      if istrue:
          resss, resultedTreee = parseToList2(s)
          true +=1
          parsingResult+= str(resss)
      else: resultedTreee=None


    print('parsingResult=')
    print(parsingResult)
    print('Quality=')
    print(true/len(sentences))
    return parsingResult,resultedTreee

def callme():
 mtext=ment.get()
 sentences=[]
 sentences.append(str(ment.get()))
 sentences.append(str(ment5.get()))

 finalResult,basicTree=parse(sentences)
 if basicTree is None:
     mlabel2=Label(mGui, text="Sorry, we did not recognised your command. Please, repeat again in a clearer way",wraplength=700, anchor= CENTER).pack()
 else:
     mlabel2=Label(mGui, text=finalResult,wraplength=700)
     mlabel2.pack()
 drawing(basicTree)
 return

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def stt2():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        s=r.recognize_google(audio)
        ment5.set(s)
        #print("You said: " + s)

    except sr.UnknownValueError:
        ment5.set("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        ment5.set("Could not request results from Google Speech Recognition service; {0}")

def GenGui():
    product()
    global mGui
    mGui= Tk()
    global ment
    ment=StringVar(mGui)
    global ment5
    ment5=StringVar(mGui)
    #sss=stt2()
    mGui.geometry('1000x700+50+50')
    mGui.title=('Maverick Test')

    mlabel = Label(mGui,text= 'Please, write your Maverick command here').pack()

    mEntry=Entry(mGui,textvariable=ment, width= 120).pack()

    mButtonv = Button(mGui, text="Enter a Voice Command!", command=stt2).pack()

    mEntry2=Entry(mGui,textvariable =ment5, width= 120).pack()

    mButton = Button(mGui, text="Parse the Command", command=callme).pack()


    mGui.mainloop()

def drawing(tree):
    if not(tree is None):
     tree.draw()

def stt():
    # Record Audio
    global ment2
    ment2=StringVar()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        s=r.recognize_google(audio)
        mEntry2 = Entry(mGui, text=s, width=120)
        mEntry2.pack()
        print("You said: " + s)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))




GenGui()