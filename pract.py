import string
import os
import io
import pprint 
import treetaggerwrapper
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
os.chdir("D:/Data only/01")
for root,dirs,files in os.walk("."):
    for file in files:
              pathname = root + '/' + file
              textfile = open(pathname, 'r' )
              readfile=textfile.read()
              no_punc=""
              x=""
              for char in readfile:
                 if char not in string.punctuation:
                      no_punc=no_punc+char
              wordss=no_punc.lower().split()
              words=['<S>']+wordss
              words=words+['<E>']
              for word in words:
                 withoutstopwordremoved=open('stopwords not removed.txt','a')
                 withoutstopwordremoved.write(word+"\n")
                 withoutstopwordremoved.close()
              stopword=set(stopwords.words('english'))
              for character in words:
               if character in stopword:
                 character.replace(character," ").split()
               else:
                  removedstopword=character
                  stopwordremoved=open('all stopwords removed.txt','a')
                  stopwordremoved.write(removedstopword+"\n")
                  stopwordremoved.close() 
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='C:\TreeTagger')
    tags = tagger.tag_file('stopwords not removed.txt')
    lemmas=open('tags','a')
    lemmas.write(tags)
    lemmas.close()
    pprint.pprint(tags)
   

                

            
               