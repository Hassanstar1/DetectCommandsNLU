import nltk
import sys
import pickle
from sys import exit

pos_SMSs = [('I love this car', 'positive'),
              ('I will be glad to see you dad', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive'),
              ('Going well', 'positive'),
              ('Thank you', 'positive'),
              ('Hope you are doing well', 'positive'),
              ('I am very happy', 'positive'),
              ('Good for you', 'positive'),
              ('It is all good. I know about it and I accept it.', 'positive'),
              ('This is really good!', 'positive'),
              ('Tomorrow is going to be fun.', 'positive'),
              ('Smiling all around.', 'positive'),
              ('These are great apples today.', 'positive'),
              ('How about them apples? Thomas is a happy boy.', 'positive'),
              ('Thomas is very zen. He is well-mannered.', 'positive')]

neg_SMSs = [('I do not like this car', 'negative'),
('I feel terrible after the course dad', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('I am a bad boy', 'negative'),
              ('This is not good', 'negative'),
              ('I am bothered by this', 'negative'),
              ('I am not connected with this', 'negative'),
              ('Sadistic creep you ass. Die.', 'negative'),
              ('All sorts of crazy and scary as hell.', 'negative'),
              ('Not his emails, no.', 'negative'),
              ('His father is dead. Returned obviously.', 'negative'),
              ('He has a bomb.', 'negative'),
              ('Too fast to be on foot. We cannot catch them.', 'negative')]

SMSs = []
for (words, sentiment) in pos_SMSs + neg_SMSs:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    SMSs.append((words_filtered, sentiment))

def get_words_in_SMSs(SMSs):
    all_words = []
    for (words, sentiment) in SMSs:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

word_features = get_word_features(get_words_in_SMSs(SMSs))

training_set = nltk.classify.apply_features(extract_features, SMSs)
classifier = nltk.NaiveBayesClassifier.train(training_set)

# optional to save your classifier so you can load it elsewhere without having to rebuild training set every time
save_classifier = open("SMSposneg.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# optional load from classifier that was saved previously
# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()

runSMSs = []  # setup to import a list of SMSs here if you wish into a python list
if len(sys.argv) > 1:  # if param passed 4 name of text file w/ list of SMSs
    SMSfile = sys.argv[1]
    with open(SMSfile, "r") as ins:
      for line in ins:
        runSMSs.append(line)
runSMSs.append('It was a terrible match')  # test SMS incase
poscount = 0
negcount = 0
for SMSt in runSMSs:
  valued = classifier.classify(extract_features(SMSt.split()))
  print (valued)
  if valued == 'negative':
    negcount = negcount + 1
  else:
    poscount = poscount + 1
    print ('Positive count: %s \nNegative count: %s' % (poscount,negcount))
  exit()