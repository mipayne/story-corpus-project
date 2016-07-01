# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:26:43 2016

@author: Madelyn
"""
  
def modify_words2(final_words_modify_set, custom_stopwords, removed_words):
    '''
    removes too simple words from final_words list
    Inputs: word list, custom_stopwords list, removed_words list
    
    Outputs: modified word list, removed_words list
    '''
    final_words_modify2 = [x for x in final_words_modify_set if x not in custom_stopwords]
    removed_words = [x for x in final_words_modify_set if x in custom_stopwords]
    return (final_words_modify2, removed_words)