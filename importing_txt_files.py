# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:28:20 2016

@author: Madelyn
"""
from __future__ import division
import nltk
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''
#from nltk.tag.simplify import simplify_wsj_tag
'''
import nltk
with(open('/Users/Madelyn/Desktop/UROP/Story Corpus/A Cub Can.txt', 'r') as in_file):
    text = in_file.read()
    sents = nltk.sent_tokenize(txt)
    
print sents
'''

#book_file = open('/Users/Madelyn/Desktop/UROP/Story Corpus/A Cub Can.txt')
#print book_file.read()

f = open('./StoryCorpus/A Cub Can.txt')
raw = f.read()

print raw


sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
#print len(sent_tokenize_list)
print sent_tokenize_list

word_sent_token = []
#breaks each sentence into a  list of its parts
for sent in sent_tokenize_list:
    #print word_tokenize(sent)
    word_sent_token.append(word_tokenize(sent))
print '\n'
pos_tag_sent_list = []

#creates list of tuples for each part of each sentence (word, pos_tag) 
for sent in word_sent_token:
    print nltk.pos_tag(sent)
    pos_tag_sent_list.append(nltk.pos_tag(sent))
print '\n'
print pos_tag_sent_list

lem_ready_word_list = []

for sent in pos_tag_sent_list:
    for tuple_pair in sent:
        word = tuple_pair[0]
        pos_tag = tuple_pair[1]
        #gives correct pos_tag
        pos_tag = get_wordnet_pos(pos_tag)
        #print pos_tag
        #makes words lowercase
        word = word.lower()
        lem_ready_word_list.append((word, pos_tag))

    
print lem_ready_word_list


final_words = []

for tuple_pair in lem_ready_word_list:
    word = tuple_pair[0]
    pos_tag = tuple_pair[1]
    if pos_tag == '':
        lem_word = wordnet_lemmatizer.lemmatize(word)
        final_words.append(lem_word)
    else:
        lem_word = wordnet_lemmatizer.lemmatize(word, pos=pos_tag)
        final_words.append(lem_word)

print final_words

    
tot_word_value = 0
word_count = 0
rejected_words = []  
 
for word in final_words:
    for key in ezsheet_dict:
        value = ezsheet_dict[key]
        if word in value:
            tot_word_value += 1
        elif:
            for key in allsheet_dict:
                value = allsheet_dict[key]
                if word in value:
                    tot_word_value += 2
                    continue #will this line prevent giving extra points if word is in two columns of 'WordCategories'?
        else:
            rejected_words.append(word)
    print word_count
print word_count

'''

lemmatized_word_list = []
for sent in simplified_list_of_lists:
    for word in sent:
        pass
        word = word.lemmatize()
        lemmatized_word_list.append((word, pos_tag))
        
for sent in lemmatized_word_list:
    for tuple_pair in lemmatized_word_list:
        pass
        #check pos_tag to match some WordCategories
        #check for word in those WordCategories
        #assign values
'''        




'''
text = "this's a sent tokenize test. this is sent two. is this sent three? \
    'is this sent three?' sent 4 is cool! Now it's your turn."

from nltk.tokenize import sent_tokenize
sent_tokenize_list = sent_tokenize(text)
print len(sent_tokenize_list)
print sent_tokenize_list

word_sent_token = []

from nltk.tokenize import word_tokenize
for sent in sent_tokenize_list:
    print word_tokenize(sent)
    word_sent_token.append(word_tokenize(sent))
    
for sent in word_sent_token:
    print nltk.pos_tag(sent)
'''    
    