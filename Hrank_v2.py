import Hrank_v3 as H3
from collections import defaultdict,Counter
import textwrap
from nltk.corpus import wordnet as wn
##############################################333
#needs to shift 
#counts the word frequencies



##########################################################################################################
#C_5 Clustering 

def Get_Clusters(fr,t6,clusters_to_write):
    f = open(clusters_to_write,'w', encoding="utf8")
    #k1
    simstr = ""
    wordlist = []
    dm = []
    for i in t6:
        a1 =wn.synsets(i)
        a2 =(a1[0])
        dm.append([])
        wordlist.append(i)
        for x in t6:
            b1 =wn.synsets(x)
            b2 =([b1][0][0])                                   
            wup1 =a2.wup_similarity(b2)         
            if wup1 is None:
                simstr+="0.0 "
                dm[-1].append(1.0)
                continue        
            dm[-1].append(1.0-wup1)
            simstr += str(wup1)+" " 
        simstr += "\n"
          
    import sklearn.cluster
    num_clusters=8
    agg = sklearn.cluster.AgglomerativeClustering(n_clusters=num_clusters, affinity='precomputed',linkage="complete")
    cluster_labels=agg.fit_predict(dm)
    k=[]
    m =[]
    d=[]
    for i in range(num_clusters):
        print ("CLUSTER-",i+1,"\n",file =f)
        print ('Frequency \t  Word \n',file =f)
        for j in range(len(cluster_labels)):
            if cluster_labels[j] == i:
                


                print("(%d) \t %s   "%(fr[t6[j]],t6[j]),file=f)         

                k.append(["cluster",i])
                k.append(t6[j])
                k.append(fr[t6[j]])
                m.append(k)

            d.append(m)
        print("\n",file=f)      
    keywords = []
    clusters = {}
    for i in range(num_clusters):
        clusters[i] = {}
        clusters[i]['clusterSize'] = 0
        clusters[i]['items'] = []

    clusterSizes = [0] * num_clusters
    for i in range(len(cluster_labels)):
        clusters[cluster_labels[i]]['clusterSize'] += fr[t6[i]]
        clusters[cluster_labels[i]]['items'].append([t6[i], fr[t6[i]]])
        clusterSizes[cluster_labels[i]] += fr[t6[i]]

    maxClusterSize=max(clusterSizes)
    maxFrequency = fr[max(fr, key=fr.get)]

    for i in range(num_clusters):
        if clusters[i]['clusterSize'] < maxClusterSize*0.3:
            continue
        keywords.append(clusters[i]['items'][0][0])
        for word in clusters[i]['items'][1:-1]:
            if word[1] > 3 and word[1] > 0.2*maxFrequency:                    
                keywords.append(word[0])       
    f.close()
    return(keywords)





##################################################################################################


def Hrank(URL):
    Text,HTML =H3.Web(URL)
    # Text pre-processing
    Clean_Text = H3.Clean_text(Text)
    #Count the words and their frequencies
    words_and_freq = H3.Calc_word_frequency(Clean_Text) 
    #POS Distribution

    (nouns,adjectives,verbs) = H3.POS_seperator(Clean_Text)
    #get top frequent 40 nouns and 2 adjectives and 1 verb 
    length_nouns = len(nouns)


    (most_frequent_40_nouns,frequencies_nouns,counts_nouns)= H3.Count_frequencies_for_POS(40,nouns) # N and POS_text

    (Adjectives_two, frequencies_adjectives, count_adjective)= H3.Count_frequencies_for_POS(2,adjectives)

    (Verb_one,frequencies_verb,count_verb) = H3.Count_frequencies_for_POS(1,verbs)

    # two seperate list Based on the WordNet

    (words_list_with_synsets, word_list_without_synsets)= H3.Get_Synsets_Score(most_frequent_40_nouns)
    

    keywords = Get_Clusters(frequencies_nouns, words_list_with_synsets,'io/Clusters.txt')
    #keywords_with_syn =list(keywords + A+V+no_syn_words)
    keywords_combine =list( keywords + Adjectives_two + Verb_one)


    return(Text,words_and_freq,nouns,adjectives,verbs, keywords_combine)


    

    #POS distributions



#################################################################################################3
def Split_text_on_space(Text):
    words =' '
    for x in Text.split():        
        text = ''.join (x)        
        words += text+' '        
    return (words)
def Write_Webpage_Text_in_txt(Text):    
    text_words =Split_text_on_space(Text)           
    good_text =textwrap.fill(text_words,140)    
    k =open('io/Text.txt','w', encoding="utf-8") # name of the file is Text.txt
    k.write(str(good_text))    
    k.close()

#########################################3
def Writing_pos_tags_in_txt(noun_text,adjective_text,verb_text):
    txt_file = open('io/POS_Text.txt','w',encoding ='utf8')    
    noun_text_combine =' '.join(noun_text)
    adjective_text_combine =' '.join(adjective_text)
    verb_text_combine =' '.join(verb_text)
    txt_file.write ('\t \t \t \t  NOUNS \n \n')

    txt_file.write(noun_text_combine + ' \n \n')
    txt_file.write('-------------------------------------------------------------------------------------------------------\n \n')
    txt_file.write ('\t \t \t \t  ADJECTIVES \n \n')

    txt_file.write(adjective_text_combine + ' \n \n')
    txt_file.write('-------------------------------------------------------------------------------------------------------\n \n')
    txt_file.write ('\t \t \t \t  VERBS \n \n')

    txt_file.write(verb_text_combine + ' \n \n')
    txt_file.write('-------------------------------------------------------------------------------------------------------\n \n')
    txt_file.close()
############################################################################################################
def Write_Word_and_Freq_in_txt(words_and_freq):
    with open ('io/Word_Frequency.txt','w',encoding="utf-8")as f:
        from prettytable import PrettyTable
        T_count =PrettyTable(["Word","Frequency"])    
        for x,i in words_and_freq.items():  
            T_count.add_row([x,i])    
        f.write(str(T_count))
###########################################################################################
# input url read from the txt file
file_open = open ('io/url.txt','r')
URL = file_open.readline()
if len(URL)<1:
    URL = 'http://bbc.com'
file_open.close()
############################################################
# hrank function main program -1
(Text,words_and_freq,nouns,adj,verb, keywords_combine) = Hrank(URL)  

#-2 write text of webpage in txt file 
Write_Webpage_Text_in_txt(Text)

#-3 write nouns,adjectives and verbs in POS_Text file 
Writing_pos_tags_in_txt(nouns,adj,verb)

#-4 Write word and frequency in the table form
Write_Word_and_Freq_in_txt(words_and_freq)


#-5 Clusters information 8 clusters

#6 keywords 
txt_keywords = open('io/Keywords.txt','w',encoding = 'utf-8')
for x in keywords_combine:
    txt_keywords.write(x + '\n')
txt_keywords.close()

####################################################
