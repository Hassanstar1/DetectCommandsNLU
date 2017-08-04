import traceback

import nltk
import sys
from tkinter import *
from nltk import *
import _tkinter
from nltk.tree import *
from nltk.draw import tree
from tkinter import *
import speech_recognition as sr
import pygame
from gtts import gTTS
import os
import time
from translate import Translator


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

Command -> CommandVerb Keyword TEXT1 Keyword TEXT1 SMSInitial SMS

CommandVerb -> "send" | "text" | "inform" | "tell" | "texting" | "maverick" CommandVerb | "must" "be" "sent"
Keyword -> "to" | "for" | "into" | "repeat" | "at" | "say" | "notify" | "an" | "a" |"in"
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
    print(tree)
    #drawing(tree)
    global ctree
    ctree=''
    for subtree in tree.subtrees():
        if subtree.label() == 'CommandVerb':
            ctree+= ("You want to  ")
            ctree+=str(subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            ctree +="\n Message"
        elif subtree.label() == 'SMS':
            ctree +=''
            ctree +=str(subtree.leaves())
        elif subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'an':
                ctree +='\n Intent '
            if subtree.leaves()[0] == 'in':
                ctree +='\n Language '
            elif subtree.leaves()[0] == 'to':
                ctree +='\n The receiver is'
            elif subtree.leaves()[0] == 'at':
                ctree +='\n Time '
            elif subtree.leaves()[0] == 'repeat':
                ctree +='\n Frequency '
            elif subtree.leaves()[0] == 'say':
                ctree +='\n with the additional command :'
        elif subtree.label() == 'TEXT1':
            ctree +=str(subtree.leaves())
    return ctree

def whLang(tree):
    ctree=''
    for subtree in tree.subtrees():
        if subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'an':
                continue
            elif subtree.leaves()[0] == 'in':
                ctree +='\n Language '
            elif subtree.leaves()[0] == 'to':
                continue
            elif subtree.leaves()[0] == 'at':
                continue
            elif subtree.leaves()[0] == 'repeat':
                continue
            elif subtree.leaves()[0] == 'say':
                continue
        elif subtree.label() == 'TEXT1':
            ctree +=str(subtree.leaves())
    return ctree

def whatContent(tree):
    #drawing(tree)
    ctree = ''
    for subtree in tree.subtrees():
        if subtree.label() == 'CommandVerb':
            ctree += ("You want to  ")
            ctree += str(subtree.leaves())
        elif subtree.label() == 'SMSInitial':
            ctree += "\n Message"
        elif subtree.label() == 'SMS':
            ctree += ''
            ctree += str(subtree.leaves())
        elif subtree.label() == 'Keyword':
            if subtree.leaves()[0] == 'an':
                ctree += '\n Intent '
            if subtree.leaves()[0] == 'in':
                ctree += '\n Language '
            elif subtree.leaves()[0] == 'to':
                ctree += '\n The receiver is'
            elif subtree.leaves()[0] == 'at':
                ctree += '\n Time '
            elif subtree.leaves()[0] == 'repeat':
                ctree += '\n Frequency '
            elif subtree.leaves()[0] == 'say':
                ctree += '\n with the additional command :'
        elif subtree.label() == 'TEXT1':
            ctree += str(subtree.leaves())
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

    try:
        ss= maverick_nlu_parser.parse(command_tokens)
        if not ss is None:
            return ss
        else:
            return "Note solved"
    except Exception as e:
        return traceback.format_exception(*sys.exc_info())


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
 if(len(str(ment.get))>1):
  sentences.append(str(ment.get()))
 elif(len(str(ment5.get))>1):
  sentences.append(str(ment5.get()))

 finalResult,basicTree=parse(sentences)
 """
 ctree = ''
 for subtree in basicTree.subtrees():
      if subtree.label() == 'Keyword':
         if subtree.leaves()[0] == 'to':
             ctree += '\n Receiver'
         elif subtree.leaves()[0] == 'at':
             ctree += '\n Time'
         elif subtree.leaves()[0] == 'repeat':
             ctree += '\n Frequency'
         elif subtree.leaves()[0] == 'say':
             ctree += '\n additional say :'
     elif subtree.label() == 'TEXT1':
         ctree += ''
         ctree += str(subtree.leaves())
 """
 if basicTree is None:
     mlabel2=Label(mGui, text="Sorry, we did not recognised your command. Please, repeat again in a clearer way",wraplength=700, anchor= CENTER).pack()
     ment6.set("Sorry, we did not recognised your command. Please, repeat again in a clearer way")
 else:
     ment6.set("Do you want to do the following? \n" + finalResult + "\n \n If you argree say yes or ok ")
     mlabel2=Label(mGui, text=ment6.get(),wraplength=700, anchor= CENTER).pack()
     """
     stt3()
     if "yes" in ment.get() or "ok" in ment.get():
         mlabel2 = Label(mGui, text="Your Message is sent with the following contents:\n"+ finalResult, wraplength=700)
         mlabel2.pack()
     """
     yousaid(basicTree)
 #drawing(basicTree)
 """
 finalResult = finalResult.replace("Result is :", " ")
 finalResult = finalResult.replace("["," ")
 finalResult = finalResult.replace("]"," and ")
 finalResult = finalResult.replace("'"," ")
 finalResult = finalResult.replace(","," ")
 ment6.set("Do you want to do the following?"+mtext)
 """

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
    try:
        s=r.recognize_google(audio)
        ment.set(s)
        print("You said: " + s)

    except sr.UnknownValueError:
        ment.set("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        ment.set("Could not request results from Google Speech Recognition service; {0}")


def stt3():
    # enter the name of usb microphone that you found
    # using lsusb
    # the following name is only used as an example
    mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
    # Sample rate is how often values are recorded
    sample_rate = 48000
    # Chunk is like a buffer. It stores 2048 samples (bytes of data)
    # here.
    # it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    # Initialize the recognizer
    r = sr.Recognizer()

    # generate a list of all audio cards/microphones
    mic_list = sr.Microphone.list_microphone_names()

    # the following loop aims to set the device ID of the mic that
    # we specifically want to use to avoid ambiguity.
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    # use the microphone as source for input. Here, we also specify
    # which device ID to specifically look for incase the microphone
    # is not working, an error will pop up saying "device_id undefined"
    with sr.Microphone(device_index=1, sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        # listens for the user's input
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            ment.set(text)

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            ment.set("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            ment.set("Could not request results from Google Speech{0}".format(e))

def trans(t,lang):
    translator = Translator(to_lang=lang)
    translation = translator.translate(t)
    return translation

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def yousaid(tree):
    theCommandText =str(ment.get())
    if "french" in theCommandText:
        language="fr"
    if "arabic" in theCommandText:
        language="ar"
    if "chinese" in theCommandText:
        language="zh"
    pos=find_str(str(ment.get()),"content")
    text=theCommandText[pos+7:]
    print("text = "+ text)
    text = trans(text,language)
    tts = gTTS("do you want to send the following content?", lang="en", slow=False)
    file="enginto.mp3"
    tts.save(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    print ("Start en : %s" % time.ctime())
    time.sleep(3)
    print ("End en : %s" % time.ctime())
    pygame.mixer.stop()
    pygame.mixer.quit()
    os.remove(file)

    tts = gTTS(text, lang=language, slow=False)
    file="hh2.mp3"
    tts.save(file)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    print ("Start : %s" % time.ctime())
    time.sleep(15)
    print ("End : %s" % time.ctime())
    pygame.mixer.stop()
    pygame.mixer.quit()
    os.remove(file)
    print("File Removed!")

def GenGui():
    product()
    global mGui
    mGui= Tk()
    global ment
    ment=StringVar(mGui)
    global ment5
    ment5=StringVar(mGui)
    global ment6
    ment6=StringVar(mGui)
    #sss=stt2()
    mGui.geometry('1000x700+50+50')
    mGui.title=('Maverick Test')

    mlabel = Label(mGui,text= 'Please, write your Maverick command here').pack()

    ment.set("send to Sam in arabic content please help me")
    mEntry=Entry(mGui,textvariable=ment, width= 120).pack()

    mButtonv = Button(mGui, text="Enter a Voice Command!", command =combine_funcs(stt3,callme,yousaid)).pack()

    #mEntry2=Entry(mGui,textvariable =ment5, width= 120).pack()

    mButton = Button(mGui, text="Process the textual command", command=combine_funcs(callme,yousaid)).pack()

    mButton = Button(mGui, text="Just parse it!", command=combine_funcs(callme)).pack()

    #mButtonStt = Button(mGui, text="Check what you said", command=yousaid).pack()
    mGui.mainloop()

def drawing(tree):
    if not(tree is None):
     tree.draw()

GenGui()