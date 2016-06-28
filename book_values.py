# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:25:07 2016

@author: Madelyn
"""
#more updated
#does nothing with rejected words; need to figure out how to handle rejected words
#allsheet_dict = {'Nouns':[u'clouds', u'face', u'animal', u'rainbow'], 'Animals':[u'goat', u'animal', u'octopus'], 'Negatives':["don't"]}

#final_words = [u'face', u'animal', "don't"]

import modify_dictionary_from_excel
print ezsheet_dict
import importing_txt_files 


def calculate_book_values(input_list, dictionary, word_point, tot_word_value, word_key_pair_dict):
    remain_list = []
    for word in input_list:
        key_list = []
        point_awarded = 0
        for key in dictionary:
            #stops code from searching all keys if word is already found\
            #   prevents double counting if word is in multiple keys
            if word in dictionary[key]:
                if not point_awarded:
                    tot_word_value += word_point
                    point_awarded = 1
                key_list.append(key)
        
        if not key_list:
            remain_list.append(word)
        else:
            word_key_pair_dict[word] = key_list
#            print 'word: ' + word + '  keys: '
#            print word_key_pair_dict[word]
            
    return (tot_word_value, remain_list, word_key_pair_dict)
 

final_words = importing_txt_files.import_txt()
#print final_words
final_words = set(final_words)

rejected_words = [] 
check_hard_list = []

tot_word_value = 0
word_count = len(final_words)
   
word_key_pair_dict = {}    

tot_word_value, check_hard_list, word_key_pair_dict = \
    calculate_book_values(final_words, ezsheet_dict, 1, tot_word_value, word_key_pair_dict)

tot_word_value, rejected_words, word_key_pair_dict = \
    calculate_book_values(check_hard_list, allsheet_dict, 2, tot_word_value, word_key_pair_dict)

#print word_key_pair_dict


#print rejected_words
#print tot_word_value
avg_book_difficulty = float(tot_word_value)/word_count
#print avg_book_difficulty

'''
for word in final_words:
    if word not in rejected_words:
        print word
'''
'''
NEXT STEP:
consider average difficulty of each group ('Nouns', 'Adjectives')
scoring books on N/V/Q/S
'''

'''
for situation where whether the word is a noun/verb/etc. doesn't matter
all that matters is its difficulty
'''
'''
#book1_words = book1_words.txt
book1_words = ["happy", "superior", "sit"]
#list1 = all_list.txt
list1 = ["happy", "sad", "play", "hit", "fight", "sit"]
#list2 = easy_list.txt
list2 = ["sad", "sit"]

tot_word_value = 0
word_count = 0

for word in book1_words:
    if word in list1:
        if word in list2:
            tot_word_value += 1
        else:
            tot_word_value += 2
    else:
        tot_word_value += 3
    word_count += 1
    print word_count, word, tot_word_value,
    
avg_book_difficulty = tot_word_value/word_count
print avg_book_difficulty
'''        
