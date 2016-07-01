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
from unidecode import unidecode

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

        
f = open('./resources/converted/StoryCorpus/Hen_Pens_Joke.txt')
raw = f.read()        
#print raw
final_words = []
word_sent_token = []
pos_tag_sent_list = []
lem_ready_word_list = []


#tokenize
sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
#breaks each sentence into a  list of its parts
for sent in sent_tokenize_list:
    word_sent_token.append(word_tokenize(sent))# DOWNSIDE: breaks up contractions\
#creates list of tuples for each part of each sentence (word, pos_tag) 
for sent in word_sent_token:
    pos_tag_sent_list.append(nltk.pos_tag(sent))

propernouns=[]
for sent in pos_tag_sent_list:
    for tuple_pair in sent:
        word = tuple_pair[0] 
        pos_tag = tuple_pair[1]
        #print tuple_pair
        #print pos_tag
        if pos_tag == 'NNP':
            #print 'hi'
            propernouns.append(word)
    #propernouns = [word for word,pos in pos_tag_sent_list if pos == 'NNP']
print propernouns


def import_txt():
    '''
    tokenize, pos_tag, and lemmatize words from files in StoryCorpus
    Returns: book_words, a dictionary s.t. book_words[fileName] = list
    '''
    list_of_files = glob.glob('./resources/converted/StoryCorpus/*.txt')
    
    final_words = []
    book_words = {}
    
    for fileName in list_of_files:
        f = open( fileName)
        raw = f.read()
        
        
        final_words = []
        word_sent_token = []
        pos_tag_sent_list = []
        lem_ready_word_list = []
    
    
        #tokenize
        sent_tokenize_list = sent_tokenize(raw)#breaks raw text into list of its sentences
        #breaks each sentence into a  list of its parts
        for sent in sent_tokenize_list:
            word_sent_token.append(word_tokenize(sent))# DOWNSIDE: breaks up contractions\
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
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                final_words.append(lem_word)
                #final_words_no_pos.append((lem_word, pos_tag)) #for situation if want to individually check categories
                    #insert code to assign tags according to WordCategories.xlsx (ex: negatives, pronoun)
            #general lemmatization
            else:
                lem_word = wordnet_lemmatizer.lemmatize(word, pos=pos_tag)
                if type(lem_word) == unicode:
                    lem_word = unidecode(lem_word)
                final_words.append(lem_word)
                #final_words_new.append((lem_word, pos_tag)) ##for situation if want to individually check categories
        
        book_words[fileName] = final_words
        


    #print len(sent_tokenize_list)
    #print sent_tokenize_list
    #print pos_tag_sent_list
    #print lem_ready_word_list
    #print final_words
    
    return (book_words)
    