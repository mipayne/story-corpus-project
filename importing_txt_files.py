# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:28:20 2016

@author: Madelyn
"""
from __future__ import division
import nltk, re, pprint
from nltk import sent_tokenize, word_tokenize
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

for sent in pos_tag_sent_list:
    

'''
tokens = word_tokenize(raw)
print tokens
words = [w.lower() for w in tokens]
print words
vocab = sorted(set(words))
print vocab
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
    