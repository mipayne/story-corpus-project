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
'''
import glob
for filename in glob.glob('/resources/StoryCorpus/*.txt'):
    print filename
    f = open(filename)
    raw = f.read()
'''   

import glob

def import_txt():
    list_of_files = glob.glob('./resources/converted/StoryCorpus/*.txt')
    
    final_words = []
    book_words = {}
    
    for fileName in list_of_files:
        f = open( fileName)
        raw = f.read()
        
    #f = open('./resources/converted/StoryCorpus/.txt')
    #raw = f.read()
        final_words = []
        word_sent_token = []
        pos_tag_sent_list = []
        lem_ready_word_list = []
    
    
        #tokenize
        sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
        #breaks each sentence into a  list of its parts
        for sent in sent_tokenize_list:
            word_sent_token.append(word_tokenize(sent))# DOWNSIDE: breaks up contractions\
            #(couldn't get to work but tweet_tokenizer could potentially avoid this)
        #creates list of tuples for each part of each sentence (word, pos_tag) 
        for sent in word_sent_token:
            pos_tag_sent_list.append(nltk.pos_tag(sent))
        #pos_tag
        for sent in pos_tag_sent_list:
            for tuple_pair in sent:
                word = tuple_pair[0]
                pos_tag = tuple_pair[1]
                #gives correct pos_tag
                pos_tag = get_wordnet_pos(pos_tag)
                #makes words lowercase
                word = word.lower()
                lem_ready_word_list.append((word, pos_tag))
        
        #lemmatize
        for tuple_pair in lem_ready_word_list:
            word = tuple_pair[0]
            pos_tag = tuple_pair[1]
            #makes sure words with no equivalent wordnet pos_tag still get lemmatized
            if pos_tag == '':
                lem_word = wordnet_lemmatizer.lemmatize(word)
                final_words.append(lem_word)
                #final_words_no_pos.append((lem_word, pos_tag)) #for situation if want to individually check categories
                    #insert code to assign tags according to WordCategories.xlsx (ex: negatives, pronoun)
            #general lemmatization
            else:
                lem_word = wordnet_lemmatizer.lemmatize(word, pos=pos_tag)
                final_words.append(lem_word)
                #final_words_new.append((lem_word, pos_tag)) ##for situation if want to individually check categories
        #book_words.append(final_words)
        book_words[fileName] = final_words
        
    #print book_words

    #print len(sent_tokenize_list)
    #print sent_tokenize_list
    #print pos_tag_sent_list
    #print lem_ready_word_list
    #print final_words
    
    return (book_words)
     


'''try: 
        #tokenize
        sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
        #breaks each sentence into a  list of its parts
        for sent in sent_tokenize_list:
            word_sent_token.append(word_tokenize(sent))
        #creates list of tuples for each part of each sentence (word, pos_tag) 
        for sent in word_sent_token:
            pos_tag_sent_list.append(nltk.pos_tag(sent))
        #pos_tag
        for sent in pos_tag_sent_list:
            for tuple_pair in sent:
                word = tuple_pair[0]
                pos_tag = tuple_pair[1]
                #gives correct pos_tag
                pos_tag = get_wordnet_pos(pos_tag)
                #makes words lowercase
                word = word.lower()
                lem_ready_word_list.append((word, pos_tag))
        
        #lemmatize
        for tuple_pair in lem_ready_word_list:
            word = tuple_pair[0]
            pos_tag = tuple_pair[1]
            #makes sure words with no equivalent wordnet pos_tag still get lemmatized
            if pos_tag == '':
                lem_word = wordnet_lemmatizer.lemmatize(word)
                final_words.append(lem_word)
            #general lemmatization
            else:
                lem_word = wordnet_lemmatizer.lemmatize(word, pos=pos_tag)
                final_words.append(lem_word)
    except UnicodeDecodeError:
        story_error.append(fileName)
        
#print final_words
print story_error
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
    