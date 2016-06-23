# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:25:07 2016

@author: Madelyn
"""

'''
for situation where whether the word is a noun/verb/etc. doesn't matter
all that matters is its difficulty
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
#for getting words from google spreadsheet
import gspread

gc = gspread.authorize(credentials)

#open a worksheet from spreadsheet with one shot
wks = gc.open(WordCategories.xlsx).All

list_of_lists = wks.get_all_values()
noun_values_list = list_of_lists[0]


wks2 = gc.open(WordCategories.xlsx).Easy
easy_list_of_lists = wks2.get_all_values()
easy_noun_values_list = easy_list_of_lists[0]

matching_words = []
for word in noun_values_list:
    if word in verb_values_list:
        matching_words.append(word)
'''
