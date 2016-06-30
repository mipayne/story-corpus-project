# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:58:12 2016

@author: Madelyn
"""


#final_words = ["san", "francisco", "new", "york", "do", "n't", "we", "'ll", 'please', '.', 'it', "'s"]

#for i in len(final_words):
#    current_word = final_words[i]
#    word_before = final_words[-i]
#    if ((current_word[0].isalnum() == False:) and len(current_word) <= 4)
#        contraction = word_before + current_word
#        final_words_fixed.append(contraction)
#        for 
#        for j in len(final_words):
#            while j < (i-1) continue:
#            if final_words[j] == word_before:
#                rep_count += 1
#        final_words_fixed.remove(final_words[-i])
#    elif i == "n't":
#    else:
#        final_words_fixed.append(final_words[i])

#keep original pos_tag
#if modal, check for negate in next value

check_word_list = ["what's", "it's", "i'm", "you've", "you'll", \
    "i've", "he'd", "he's", "we'll", "you're", "i'll", "don't", \
    "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", 'san francisco', 'new york', ' cool', "let's", \
    "don't", "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", 'act- e', 'arrive ', 'sent  ']
#check_word_list = set(check_word_list)

contraction_list = ["what's", "it's", "i'm", "you've", "you'll",\
    "i've", "he'd", "he's", "we'll", "you're", "i'll", "don't", \
    "wouldn't", "wasn't", "isn't", "won't", "didn't", "doesn't",\
    "can't", "couldn't", "let's", "don't", "wouldn't", "wasn't",\
    "isn't", "won't", "didn't", "doesn't", "can't", "couldn't"]

#contraction_list = set(contraction_list)

def modify_words1(final_words):
    cntrc_mapping_dict = {'you':["'ve","'ll","'re"], 'would':["n't"],\
        'wo':["n't"], 'what':["'s"], 'we':["'ll"], 'was':["n't"], 'let':["'s"],\
        'it': ["'s"], 'is': ["n't"], 'i':["'ve","'m","'ll"], 'he':["'s","'d"],\
        'do':["n't"], 'does':["n't"], 'did':["n't"],'could':["n't"],'ca':["n't"]}
        
    new_words = []
    final_words_modify1 = final_words[:]
                
    for i in range(len(final_words)):
        if i < (len(final_words) - 1):
            current_word = final_words[i]
            next_word = final_words[i+1]
            if current_word in cntrc_mapping_dict.keys():
                for key in cntrc_mapping_dict:
                    if current_word == key:
                        for ending in cntrc_mapping_dict[key]:
                            if next_word == ending:
                                new_word = current_word + next_word
                                new_words.append(new_word)
                                final_words_modify1.remove(current_word)
                                final_words_modify1.remove(next_word)
            elif current_word == 'san':
                if next_word == 'francisco':
                    new_word = current_word + ' ' + next_word
                    new_words.append(new_word)
                    final_words_modify1.remove(current_word)
                    final_words_modify1.remove(next_word)
            elif current_word == 'new':
                if next_word == 'york':
                    new_word = current_word + ' ' + next_word
                    new_words.append(new_word)
                    final_words_modify1.remove(current_word)
                    final_words_modify1.remove(next_word)
        else: 
            break
        
    
    final_words_modify1.extend(new_words)
    return final_words_modify1

#final_words_modify1 = modify_words1(final_words)
#print final_words_modify1


#final_words_modify1
#remove duplicates
#apply custom_stopwords
#remove punctuation (without removing words with dashes and apostrophes)
 #removed_words = []
    
#    for word in final_words:
#        if word.isalnum() == False: #and len(word) <= 2:#includes "'s", punctuation, 
#            removed_words.append(word)
#            final_words.remove(word)
    
#    print final_words
#    print removed_words