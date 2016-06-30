# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:29:12 2016

@author: Madelyn
"""
#might want to use this modify before we set(list)
#NOT USED
#NOT USED
#NOT USED


#up to 20 
numeral_word_map = {'1':'one', '2':'three','3':'three', '4':'four', '5':'five', '6':'six',\
    '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven',\
    '12': 'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen',\
    '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen',\
    '20':'twenty'}

final_words = ['cool', '3']
final_words_modify4 = final_words [:]
key_count = 0

for word in final_words:
    for key in numeral_word_map:
        if word == key:
            final_words_modify4.append(numeral_word_map[key])
            final_words_modify4.remove(word)
        elif key_count == len(numeral_word_map):
            break
        else:
            key_count += 1
            
print final_words_modify4