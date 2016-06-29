# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:26:43 2016

@author: Madelyn
"""
import modify_dictionary_from_excel
custom_stopwords = modify_dictionary_from_excel.create_custom_stopword_list(allsheet_dict)

def modify_words2(final_words_modify1, custom_stopwords, stopwords_removed)
    for word in final_words_modify1:
        if word in custom_stopwords:
            stopwords_removed.append(word)
            final_words_modify1.remove(word)
    final_words_modify2 = final_words_modify1
    return (final_words_modify2, stopwords_removed)
    
        