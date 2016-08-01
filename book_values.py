# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:25:07 2016

@author: Madelyn
"""

import modify_dictionary_from_excel
import importing_txt_files 
import fixing_strings
import stopwords_modify
import punctuation_modify
import numeral_word_modify

sheet_list = []

from pyexcel.cookbook import split_a_book

split_a_book('./resources/WordCategories.xlsx', 'output.xlsx')
import glob
outputfiles = glob.glob('*_output.xlsx')#splits book to be single sheets
for file in sorted(outputfiles):
    sheet_list.append(file)#adds each new sheet to a list
    
allsheet_dict, ezsheet_dict = modify_dictionary_from_excel.create_dictionary(sheet_list)
allsheet_dict = modify_dictionary_from_excel.modify_dictionary(allsheet_dict)
ezsheet_dict = modify_dictionary_from_excel.modify_dictionary(ezsheet_dict)
custom_stopwords = modify_dictionary_from_excel.create_custom_stopword_list(allsheet_dict)

class Book(object):
    """A book in Children's StoryCorpus
    
    Attributes:
        filename: string representing location of file
        title: string representing the book's title
        word_count_with_stopwords = len(final_words_modify3)
        word_count_no_stopwords = len(final_words_modify4)
        # in easy = final_words_modify4 - check_hard_list
        # not in a list = rejected_words
        # in all = check_hard_list - rejected_words
        avg_length_final_words = final_words_modify4/len(final_words_modify4) 
     """

    def __init__(self, title, filename, word_count_with_stopwords,\
        word_count_no_stopwords, num_ez_words, num_no_list_words, num_all_words,\
        avg_length_final_words):
        """Return a new Book object"""
        self.filename = filename
        self.title = title
        self.word_count_with_stopwords = word_count_with_stopwords
        self.word_count_no_stopwords = word_count_no_stopwords
        self.num_ez_words = num_ez_words
        self.num_no_list_words = num_no_list_words
        self.num_all_words = num_all_words
        self.avg_length_final_words = avg_length_final_words
        
    def get_filename(self):
        return self.filename
        
    def get_title(self):
        return self.title
    
    def get_word_count_with_stopwords(self):
        return self.word_count_with_stopwords
        
    def get_word_count_no_stopwords(self):
        return self.word_count_no_stopwords
        
    def get_num_ez_words(self):
        return self.num_ez_words
    
    def get_num_no_list_words(self):
        return self.num_no_list_words
        
    def get_num_all_words(self):
        return self.num_all_words
        
    def get_avg_length_final_words(self):
        return self.avg_length_final_words
        
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

removed_words = []

book_words = importing_txt_files.import_txt()

#print book_words

value_dict = {}
removed_propnouns = []

#uses pos_tag to identify proper nouns and removes them from word list   
for book in book_words:
    final_words = book_words[book]
    temp_list = []
    for word in final_words:
        #print word[1]
        if word[1] != "NNP":
            temp_list.append(word[0])
        else:
            removed_propnouns.append(word[0])
    book_words[book] = temp_list
            
#print book_words
#print removed_propnouns            

book_object_list = [] 

for book in book_words:
    final_words = book_words[book]
    final_words_modify1 = fixing_strings.string_modify(final_words)
    #print 'final_words_modify1:'
    #print final_words_modify1
    #print '\n'
    final_words_modify2 = numeral_word_modify.num_modify(final_words_modify1)
    #print final_words_modify2
    bookset= set(final_words_modify2)
    book_words[book] = list(bookset)
    final_words_modify_set = book_words[book]
    
    #insert modifiers here

    final_words_modify3, removed_words = \
        punctuation_modify.punct_modify(final_words_modify_set, removed_words)
    #print 'word_count_words'
    #print final_words_modify3
    
    final_words_modify4, removed_words = \
        stopwords_modify.stopword_modify(final_words_modify3, custom_stopwords, removed_words)
    #print 'removed_words:'
#    print removed_words
    #print 'final_words_final'
    #print final_words_modify4

    if book == './resources/converted/StoryCorpus/Tap_the_Jam.txt':
        print book[34:]
        print 'word_count_words'
        print final_words_modify3
        print 'final_words_final'
        print final_words_modify4
        
    if book == './resources/converted/StoryCorpus/The_Ram_and_The_Jam.txt':
        print book[34:]
        print 'word_count_words'
        print final_words_modify3
        print 'final_words_final'
        print final_words_modify4
    
    if book == './resources/converted/StoryCorpus/The_Dinosaur_Who_Lived_In_My_Backyard.txt':
        print book[34:]
        print 'word_count_words'
        print final_words_modify3
        print 'final_words_final'
        print final_words_modify4
    rejected_words = [] 
    check_hard_list = []
    
    tot_word_value = 0
    word_count_with_stopwords = len(final_words_modify3)#word_count includes stopwords(value = 0)
        #maybe make it so it includes only certain stopwords?
    word_count_no_stopwords = len(final_words_modify4)
   
    word_key_pair_dict = {}    
    
    tot_word_value, check_hard_list, word_key_pair_dict = \
        calculate_book_values(final_words_modify4, ezsheet_dict, 1, tot_word_value, word_key_pair_dict)
    
    tot_word_value, rejected_words, word_key_pair_dict = \
        calculate_book_values(check_hard_list, allsheet_dict, 2, tot_word_value, word_key_pair_dict)
    
    #print '\n'
    #print 'word_key_pair_dict'
    #print word_key_pair_dict
    
    
    #print 'rejected_words:'
    #print rejected_words
    
    for word in rejected_words:
        tot_word_value += 3
        
    #print 'tot_word_value:'
    #print tot_word_value
    avg_book_diff_with_stopwords = float(tot_word_value)/word_count_with_stopwords
    avg_book_diff_no_stopwords = float(tot_word_value)/word_count_no_stopwords
    #print 'average book value:'
    #print avg_book_difficulty
    value_dict[book] = (tot_word_value, word_count_no_stopwords, avg_book_diff_no_stopwords, word_count_with_stopwords, avg_book_diff_with_stopwords)
    
    #for class change
    filename = book
    title = book[34:]
    word_count_with_stopwords = float(len(final_words_modify3))
    word_count_no_stopwords = float(len(final_words_modify4))
    num_ez_words = word_count_no_stopwords - len(check_hard_list)
    num_no_list_words = len(rejected_words)
    num_all_words = len(check_hard_list) - num_no_list_words
    len_count = 0
    for word in final_words_modify4:
        len_count += len(word)
    avg_length_final_words = len_count/word_count_no_stopwords




       


    x = Book(book[34:], book, word_count_with_stopwords,\
        word_count_no_stopwords, num_ez_words, num_no_list_words,\
        num_all_words, avg_length_final_words)
    
    print x.get_filename()
    
    book_object_list.append(x)
    

for book in book_object_list:
    book.get_title()
    if book.get_title() == 'The_Ram_and_The_Jam.txt':
        print "Wcount w/ Stopwords"
        print book.get_word_count_with_stopwords()
        print "Wcount"
        print book.get_word_count_no_stopwords()
        print "Easy words: ", book.get_num_ez_words()
        print "All words: ", book.get_num_all_words()
        print "No_list words: ", book.get_num_no_list_words()
        print "Avg word length: ", book.get_avg_length_final_words ()
        
        




#clean return values

for book in value_dict:
    book_name = book[34:]
#    print book_name
#    tot_word_value, word_count, avg_book_diff, word_count_stop, avg_book_diff_stop = value_dict[book]
#    print "Total Value: ", tot_word_value
#    print "Total Words (no stopwords): ", word_count
#    print "Total Words (stopwords): ", word_count_stop
#    print "Difficulty (no stopwords): ", avg_book_diff
#    print "Difficulty (stopwords): ", avg_book_diff_stop
#    print "\n"
#print value_dict
#print len('./resources/converted/StoryCorpus/')

ordered_list = []

for book in value_dict:
    book_name = book[34:]
    tot_word_value, word_count, avg_book_diff, word_count_stop, avg_book_diff_stop = value_dict[book]
    tuple_count = 0
    first_book = False
    if len(ordered_list) == 0:
        #print "first_book"
        first_book = True
        ordered_list.append((book_name, avg_book_diff))
    #print ordered_list
    #print len(ordered_list)
    for tuple_pair in ordered_list:
        temp_list = []
        if first_book == True:
            break
        tuple_count += 1
        if avg_book_diff > tuple_pair[1]:
            temp_list = ordered_list[:(tuple_count-1)]
            temp_list.append((book_name, avg_book_diff))
            temp_list.extend(ordered_list[(tuple_count-1):])
            ordered_list = temp_list[:]
            break
        elif tuple_count == len(ordered_list):
            ordered_list.append((book_name, avg_book_diff))
            #print ordered_list
            break
        #else:
            #print 'NO!'
            
#print ordered_list           
'''
NEXT STEP:
consider average difficulty of each group ('Nouns', 'Adjectives')
scoring books on N/V/Q/S
'''

'''
for situation where whether the word is a noun/verb/etc. doesn't matter
all that matters is its difficulty
'''
