import sys
sys.path.append('/home/tko/himat/web-docs/lib/python3.6/site-packages/')
sys.path.append('/home/tko/himat/web-docs/keywordextraction/pylibs/lib64/python3.4/site-packages/')
sys.path.append('/home/tko/himat/web-docs/lib/python3.6/site-packages/lib64/python3.6/site-packages')
sys.path.append('/home/tko/himat/web-docs/keywordextraction/pylibs/lib/python3.4/site-packages/lib/python3.4/site-packages/')
sys.path.append('/home/tko/himat/web-docs/lib/python3.6/site-packages/')
sys.path.append('/home/tko/himat/lib/python3.4/site-packages/')
#NEW LOCATION FOR PACKAGES ON SERVER
sys.path.append('/home/tko/himat/web-docs/keywordextraction/lib/python3.6/site-packages')
sys.path.append('/usr/lib/python3.4/site-packages')
sys.path.insert(0, '/home/tko/himat/web-docs/keywordextraction')
#sys.path.append('/home/tko/himat/packages/')
from collections import defaultdict 
import re 
import wikipedia
from nltk.corpus import stopwords
import numpy as np
import lxml
import math
import quandl
import urllib
import nltk
import Hrank_v3 as H3
from collections import defaultdict,Counter
import textwrap
from nltk.corpus import wordnet as wn
import quandl
import numpy as np
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
import pandas as pd 
import math
import lxml
import textwrap
import sys
import re 
from nltk.corpus import stopwords
import numpy as np
import nltk
import urllib
from bs4 import BeautifulSoup
import numpy as np
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
import pandas as pd 
import math
import textwrap
import sys
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import defaultdict,Counter

sys.path.insert(0, '/home/tko/himat/web-docs/keywordextraction')

from flask import Flask
import requests
from bs4 import BeautifulSoup

from collections import defaultdict
sys.path.append('/home/tko/himat/web-docs/keywordextraction/pylibs/lib/python3.4/site-packages/')

sys.path.append('/home/tko/himat/web-docs/keywordextraction/pylibs/lib/python3.4/site-packages/')
stp ="january use jun jan feb mar apr may jul agust dec oct nov sep dec  product continue one two three four five please thanks find helpful week job experience women girl apology read show eve  knowledge benefit appointment street way staff salon discount gift cost thing world close party love letters rewards offers special close  page week dollars voucher gifts vouchers welcome therefore march nights need name pleasure show sisters thank menu today always time needs welcome march february april may june jully aguast september october november december day year month minute second secodns".split(" ")
common_nouns='debt est dec big than who '.split(" ")

spchars = re.compile('\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\=|\\|\||\{|\[|\]|\}|\:|\;|\'|\"|\<|\,|\>|\?|\/|\.|\-')
from nltk.corpus import stopwords
english_stopwords=set(stopwords.words("english"))
import warnings
warnings.filterwarnings("ignore")
#######################################################################################################################
def Scrapper1(element):
    if element.parent.name in ['html','style', 'script', 'head',  '[document]','img']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def Scrapper2(body):                #text_from_html(body):
    soup = BeautifulSoup(body, 'lxml')      
    texts = soup.findAll(text=True)   
    name =soup.findAll(name=True) 
    visible_texts = filter(Scrapper1,texts)        
    return u" ".join(t.strip() for t in visible_texts)
#raw =Scrapper2(html)#text
def Scrapper3(text):                  #filters(text):  
    lines = (line.strip() for line in text.splitlines())    # break into lines and remove leading and trailing space on each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))# break multi-headlines into a line each
    return u'\n'.join(chunk for chunk in chunks if chunk)# drop blank lines


def Scrapper_title_4(urls):
  req = urllib.request.Request(urls, headers={'User-Agent' : "Magic Browser"})
  con = urllib.request.urlopen(req)
  html= con.read()
  title=[]
  
  soup = BeautifulSoup(html, 'lxml') 
  title.append(soup.title.string)
  return(title,urls)

def Web(urls):
  req = urllib.request.Request(urls, headers={'User-Agent' : "Magic Browser"})
  con = urllib.request.urlopen(req)
  html= con.read()  

  soup = BeautifulSoup(html, 'lxml') 
  #keywordregex = re.compile('<meta\sname= ["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')  
  raw =Scrapper2(html)
  clean_text=Scrapper3(raw) 
  return(clean_text,soup)  
  ###################################################################################################################
def Clean_text(text):
  Words =[]
  for word in text.split():       
      word = word.replace("’",' ')
      word = word.lower()
      word = spchars.sub(" ",word.strip())
      if word not in english_stopwords:
          if word not in common_nouns:
            if len(word)>1:
                  if word != "  ":
                      if word not in common_nouns:
                          if not word.isdigit():
                              if word not in english_stopwords:
                                  for x in word.split():
                                      if x not in english_stopwords and x not in common_nouns and len(x)>1 and x not in common_nouns:
                                          x = x.strip()
                                          if not x[0].isdigit():
                                            Words.append(x)                                  

  return (Words)
#############################################################################################################################
def POS_seperator(Text):
  adj=[]
  verb=[]
  nouns=[]

  for line in Text:
    tokens = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(tokens)

    
    for x,y in tagged:
      if y in ['NNP','NNPS','NNS','NN']:
        nouns.append(x)
      if y in ['JJ', 'JJR', 'JJS']:
        adj.append(x)
      if y in ['VB','VBD','VBG','VBN','VBP']:
        verb.append(x)
  return (nouns,adj,verb)

def Count_fr(words):
  token=[]
  count=[]
  fr = Counter(words)
  for t,c in fr.most_common():
    token.append(t)
    count.append(c)
  return(token,fr,count)     
def Calc_word_frequency(nouns):
    
    top_words ={}  
    word=[]
    result =[]
    fr = Counter(nouns)    
    for x,c in fr.most_common():
        word.append([x,c])
        top_words[x]=c
    return(top_words)
#################################################################

def Count_frequencies_for_POS(N,POS_text):
    Word_only=[]
    Word_frequency_only=[]
    words_and_freq = Counter(POS_text)

    for word,counts in words_and_freq.most_common(N):
        Word_only.append(word)
        Word_frequency_only.append(counts)

    return(Word_only,words_and_freq,Word_frequency_only)
################################################
def Get_Synsets_Score (most_frequent_40_nouns):
    words_list_with_synsets=[]
    word_list_without_synsets =[]
    for word in most_frequent_40_nouns:
        a1 =wn.synsets(word)
        if len(a1) > 0:
           words_list_with_synsets.append(word)
        else:
            word_list_without_synsets.append(word)
    
    return (words_list_with_synsets,word_list_without_synsets)
###################################################################################################################
#Section-04  URL Division
######################################################################################################################
def Divide_Url(url):
    from urllib.parse import urlparse 
    host=[]
    obj=urlparse(url)    
    name =(obj.hostname)
    for x in name.split('.'):
        if x.lower() not in ['','https','www','com','-','php','pk','fi','http:','http']:
            host.append(x)
    return(host)
def Urls(url):
    path=[]
    host =Divide_Url(url)   
    for x in url.split('/'):
        for i in x.split('.'):
            for d in i.split('-'):
                if d.lower() not in ['','https','www','com','-','php','pk','fi','https:','http','http:','html','htm'] and d.lower() not in host:              

                    path.append(d.lower())
    return(host,path)

##############################################################################################################################################################
#Section-   Beautiful Soup find tags features
###############################################################################################################################################
def explode(h_d):
    alt_words=[]
    if len(h_d)>0:
        for k,i in h_d.items():      
   
            for x in i:
                word=[n for n in x.split(',')]
                for x in word:
                    words=[i for i in x.split() ]
                    for x in words:
                        alt_words.append(x)
        return(alt_words)
    else:
        return(alt_words)
def get_text(soup,h):
    text=[]
    zero=[]
    for w in soup.find_all(h):
        h_text = w.text.strip()
        h_text =(h_text.lower())
        text.append(h_text)
    if len(text)!=0:
        return(text)
    else:
        return(zero)

def Extract_headerAnchorTitle(soup):
    h1_d ={}
    h2_d ={}
    h3_d ={}
    h4_d ={}
    h5_d ={}
    h6_d ={}
    a_d ={}
    title_d={}
    h1_d['h1']= get_text(soup,'h1')
    h2_d['h2']= get_text(soup,'h2')
    h3_d['h3']=get_text(soup,'h3')
    h4_d['h4']= get_text(soup,'h4')
    h5_d['h5']= get_text(soup,'h5')
    h6_d['h6']= get_text(soup,'h6')
    
    a_d['a']= get_text(soup,'a') #alt tab or anchor
    title_d['title']= get_text(soup,'title')  #CALLing       
    H1=explode(h1_d)
    H2=explode(h2_d)
    H3=explode(h3_d)
    H4=explode(h4_d)
    H5=explode(h5_d)
    H6=explode(h6_d)    
    A=explode(a_d)    
    T= explode(title_d)
    
   
    return(H1,H2,H3,H4,H5,H6,A,T)
######################################################################################################################## 
#Section-6 Writing reading file in txt and csv
#######################################################################################################################

def Write(Text):
    words =' '
    for x in Text:
        text = '  '.join (x.split())
        words += text+' '
    return (words)
def Writing_csv(dic,file):
    import csv  
    f = open(file,'w',encoding='utf-8')
    writer = csv.writer(f)
    for k in dic.items():
        writer.writerow(k)

def Read_Txt(file):
    f=open(file,'r')
    read = f.readlines()
    f.close()
    gt =[]
    for x in read:
        URL= (x.split()[0])
        Gt =x.replace(URL,'')
               
        for y in Gt.split():
            y =y.strip("\n")
            y=y.strip(",")
            if y==" " or y is None:
                continue
            gt.append(y.lower())            
    return(URL,gt)  
######################################################################################################## 
#section-07 Score features
#Features_Score inputs candidate word,words of feature list and score,name of feature
#returns total score and features name 

#########################################################################################################
def Feature_Score(candidate_word,feature_words,score):
    total_score=0
    score_single_time =0
    

    for word_feature in feature_words:
        if word_feature ==candidate_word:
            total_score+=score
            score_single_time =score
                
    return(score_single_time) 
    


def Score_Features(word_fr,H1,H2,H3,H4,H5,H6,anchor,title,url_part1,url_parts,text_length):    
    word_score ={} 
            
    feature_names=defaultdict(list)
   
    #score = [score_h1,score_h2,score_h3,score_h4,score_h5,score_h6]
   

    for word,fr in word_fr.items(): 
        score_h1 = Feature_Score(word,H1,6)
        score_h2 = Feature_Score(word,H2,5)
        score_h3 = Feature_Score(word,H3,3)
        score_h4 = Feature_Score(word,H4,2)
        score_h5 = Feature_Score(word,H5,2)
        score_h6 = Feature_Score(word,H6,2)

        score_anchor = Feature_Score(word,anchor,1)
        score_title = Feature_Score(word,title,6)

        score_url_host = Feature_Score(word,url_part1,5)
        score_url_query = Feature_Score(word,url_parts,4)

        if text_length<50:
            tf_score =((fr/100)*50)
        else:
           tf_score=((fr/100)*20)    

        #f_score =s+s2+s3+s4+s5+s6+s7+s8+s9+s10+tf_score
        final_score_word = (score_h1+ score_h2+ score_h3+ score_h4+ score_h5+ score_h6+ score_anchor+ score_title+ score_url_host+ score_url_query+ tf_score)
        
        #Get the names of tags a word occurs work for display bbc['h1','h2']
        '''

        score_list = [score_h1,score_h2,score_h3,score_h4,score_h5,score_h6,score_anchor,score_title,score_url_host, score_url_query]        
        feature_name =['h1','h2','h3','h4','h5','h6','A','T','URL-H','URL-Q']
        for x in range(len(score_list)):
            if score_list[x]>0:                
                feature_names[word].append([feature_name[x],fr,final_score_word])
       '''

        

        word_score[word] = final_score_word
        #pr12[x]=final_pr
            
    return(word_score)




#############################################################################################
#Section-09 Text blob and spacy models
def blob_functions(text):
    from textblob import TextBlob
    text_blob =TextBlob(text)
    tokens = text_blob.words
    sentences =text_blob.sentences
    noun_phrases =text_blob.noun_phrases
    count_noun_phrases = text_blob.np_counts
    #polarity from -1 to 1
    polarity = text_blob.polarity
    hight_polarity_senetences=[]
    hight_subjectivity_senetences =[]
    #print (polarity)
    for x in sentences:
        if x.polarity>0.5:
            hight_polarity_senetences.append(x)
    subjectivity =text_blob.subjectivity
    for  x in sentences:
         if x.subjectivity>0.5:
            hight_subjectivity_senetences.append(x)

    sentiment =text_blob.sentiment # subjectivity and polarity of the words
    # translate any langugage text into other language
    #list of language available on blob documentations

    translated_language = text_blob.translate(to='es')
    n_grams = text_blob.ngrams(n=2)
    

###############################################################################################
'''
import wikipedia 
#summary= (wikipedia.summary('recall'))
#few_lines_summary =(wikipedia.summary('recall',sentences =5))
name =input('Enter your name')
print(wikipedia.summary(name))
ny = wikipedia.page("New York")
title =ny.title
url =ny.url
contents =ny.content
images= ny.images[0]
links =ny.links[0]
'''
def Wiki_TF(keywords_list):       
    tf_score_for_word=defaultdict(list)
    word_tf =[]

    import csv
    #with open('/usr/local/www_root/paikka/shah/idf_terms.csv','r') as csv_file:                    # extracted by wikipedia documents
    with open('Wicki.csv','r',encoding="utf8") as csv_file:                                                         #extracted txt files

        csv_reader =csv.reader(csv_file)
        for x in csv_reader:            
            if x[1] in keywords_list:
                tf_score_for_word[x[1]]=x[2]
               

    return (tf_score_for_word)


######################################################################################################
def Feature_Score(candidate_word,feature_words,score):
    total_score=0
    score_single_time =0
    

    for word_feature in feature_words:
        
        if word_feature ==candidate_word:
            
            #total_score+=score
            score_single_time = score
                
    return(score_single_time)
           
def Tf_Score(fr,text_length):
    if text_length<50:
        tf_score =((fr/100)*50)
    else:
        tf_score=((fr/100)*20) 
    return (tf_score)

#x[0]=word_in wikipedia  x[1]= tf in wikipedia generated from csv file
          


def Remove_duplicates_GT(l):
    new_list =[]
    [new_list.append(x) for x in l if x not in new_list]
    return (new_list)

def Clean_CSV_Files(words):
    w=[]
    import string
    from string import digits
    exclude = set(string.punctuation)
    if type(words) is not list:
        words = [(spchars.sub(" ", i)).replace('\n','').strip().lstrip(digits)for i in words.split(',') if i not in exclude ]
    else:
        words =[(spchars.sub(" ", i)).replace('\n','').strip().lstrip(digits)for i in words if i not in exclude ]

    for x in words:
        if len(x)>0:
            w.append(x)
    return(w)