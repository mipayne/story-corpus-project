# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:47:42 2016

@author: Madelyn
"""
import re
#final_words = ["'please", '.', 'it', "'s", "''", "``", "isn't"]

def modify_words3(final_words, removed_words):
    '''
    removes punctuation from long strings, removes strings with punctuation
    with length <= 3, assuming they are not real words
    Inputs: word list, removed_words list
    Outputs: modified word list, removed_words list
    '''
    contraction_list = ["what's", "it's", "i'm", "you've", "you'll",\
        "i've", "he'd", "he's", "we'll", "you're", "i'll", "don't", \
        "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
        "can't", "couldn't", "let's", "don't", "wouldn't", "wasn't",\
        "isn't", "won't", "didn't", "doesn't", "can't", "couldn't"]
    
    final_words_modify3 = final_words[:]    
    for word in final_words:
        #finds words with punctuation
        if (word.isalnum() == False):
            #for long words, punctuation removed; really short words are removed
            if (len(word) > 3 and word not in contraction_list):
                #print word
                new_word = re.sub(r'[^\w]','', word)
                #print new_word
                final_words_modify3.append(new_word)
                removed_words.append(word)
                final_words_modify3.remove(word)
            elif len(word) <= 3:#includes "'s", punctuation, "''", "``"
                removed_words.append(word)
                final_words_modify3.remove(word)
        
    return (final_words_modify3, removed_words)

#print 'removed_words:'
#print removed_words
#print 'final_modify3'
#print final_words_modify3

    #final_words_modify1
    #remove duplicates
    #apply custom_stopwords
    #remove punctuation (without removing words with dashes and apostrophes)
     #removed_words = []
    