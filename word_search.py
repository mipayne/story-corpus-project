# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:55:30 2016

@author: Madelyn
"""
word_categories_list = []


for key in my_dict:
    if key 
    word_categories_list.append(key)

my_dict = {'Nouns': [ u'program', u'hole', u'bit', u'loss', u'role'] \
,'Adjectives': [u'happy', u'nearby', u'successful', u'busy']}

postag_sent_list = [[('It', 'PRP'), ('can', 'MD'), ('dip', 'VB'), ('.', '.')],\
    [('With', 'IN'), ('help', 'NN'), (',', ','), ('a', 'DT'), ('cub', 'NN'), ('can', 'MD'), ('grow', 'VB'), ('up', 'RP'), ('.', '.')]]
word_postag_list = [('Love','NN'), ('happy','adj')]

'''
for key in my_dict:
    value = my_dict[key]
    for word in value:
        print word #accessing the individual words of each header
'''
count = 0
temp_list = []

#for subclasses in categories (ex: Nouns > Animals) label both as the corresponding tag \
#   so the word is searched for through all classes that are nouns

pos_mapping_dict = {'Nouns': 'NN', 'Adjectives': 'adj', 'Animals': 'NN'}
#names the two indices of each tuple_pair in the list
    #maybe make the values lists to allow {'Verbs' : [VB, VBD, VBG, VBN, VBP, VBZ]}
    #look for built-in function that collects all 'Verb' pos_tags, all 'Noun' pos_tags etc. 
for tuple_pair in word_postag_list:
    word = tuple_pair[0]
    pos_tag = tuple_pair[1]
    #makes words lowercase
    word = word.lower()
    temp_list.append((word, pos_tag))
    word_postag_list = temp_list
    #iterates through each key in pos_mapping_dict
    for mapping_key in pos_mapping_dict:
        value = pos_mapping_dict[mapping_key] #value is a value in the pos_mapping_dict
        # will search for word in the appropriate key of my_dict \
        #   if pos_tag is mapped to a my_dict key 
        if pos_tag == value:
            if word in my_dict[mapping_key]:
                print word
                count += 1 #gives a value of 1 for each word found in my_dict

print count

'''
temp_list = []

for tuple_pair in word_postag_list:
    word = tuple_pair[0]
    pos_tag = tuple_pair[1]
    word = word.lower()
    temp_list.append((word, pos_tag))
    word_postag_list = temp_list
    print word
print word_postag_list
'''     
'''    
for tuple_pair in book_word_tuple_list:
    word = tuple_pair[0]
    for key in my_dict:
        value = my_dict[key]
        if word in value:
            print word
'''

##dictionary cleans working correctly check
#count = 0
#for word in sheet1_word_count:
#    for key in sheet1_dict:
#        if word == key:
#            count += 1
#            
#print count #gave 12! ( which is what we want because we took out 'Total Words' key)
