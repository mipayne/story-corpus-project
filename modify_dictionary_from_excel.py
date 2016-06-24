# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:00:43 2016

@author: Madelyn
"""

'''
for key in my_dict:
    value = my_dict[key]
    for word in value:
        print word #accessing the individual words of each header
'''
#the process works but takes forever (2.0694129467 seconds)
##import time
##start_time = time.time()
import pyexcel
sheet_list = []

from pyexcel.cookbook import split_a_book
split_a_book('./resources/WordCategories.xlsx', 'output.xlsx')
import glob
outputfiles = glob.glob('*_output.xlsx')#splits book to be single sheets
for file in sorted(outputfiles):
    sheet_list.append(file)#adds each new sheet to a list
##print("--- %s seconds ---" % (time.time() - start_time))
    
print sheet_list
print sheet_list[0]
for i in sheet_list:
    if i == 'All_output.xlsx':
        allsheet = pyexcel.get_sheet(file_name = sheet_list[0], name_columns_by_row=0)
        allsheet_od = allsheet.to_dict() 
        allsheet_dict = dict(allsheet_od)
    elif i == 'Easy_output.xlsx':
        ezsheet = pyexcel.get_sheet(file_name = sheet_list[1], name_columns_by_row=0)
        ezsheet_dict = dict(ezsheet.to_dict())
    else:
        print "You don't have the appropriate sheet names"
 
#print allsheet_dict
#print ezsheet_dict


word_count_dict_All = {}
word_count_dict_Easy = {}

def make_word_count_dict(my_dict, word_count_dict):
    '''
    Takes word count from each category and puts them into their own dictionary
    
    Inputs: the original dictionary and the resulting word_count dictionary
    Outputs: returns word_count dictionary and original dictionary
    '''
    for key in my_dict:
        value = my_dict[key]
        word_count = int(value[0])
        word_count_dict[key] = word_count
    return word_count_dict



def clean_dict(my_dict):
    '''
    Removes empty spaces ('') from a dictionary
    
    Inputs: dictionary
    Outputs: revised dictionary
    '''
    for key in my_dict:
        value = my_dict[key]
        for elm in value:
            if type(elm) == long:
                value.remove(elm)#gets rid of first elm of each value list which is word_count
        while '' in value:#gets rid of blanks in all value lists
            value.remove('')
    del my_dict['Total Words'] #gets rid of total words key
        #for word in value:
           #str(word) #does this do anything?
    return my_dict


#b = clean_dict(my_dict)
#print b

def extra_clean_dict(my_dict):
    '''
    Removes the word count from the dictionary
    Is separated from first clean because some 1st values were not numbers
    '''
    for key in my_dict.keys():
        if key == '': #takes care of case where key is blank for some reason
            del my_dict[key]
    return my_dict
    
def lower_dict(my_dict):
    '''
    str in the lists for each key are made lowercase
    '''
    for key in my_dict:
        y = []
        for x in my_dict[key]:
            #excel automatically makes 'True' and 'False' bools; can't lower bools
            # --> if statement makes them unicode strings again
            if type(x) == bool:
                x = unicode(x)
            x = x.lower()
            y.append(x)
        my_dict[key] = y
    return my_dict

allsheet_dict = extra_clean_dict(allsheet_dict)
allsheet_word_count = make_word_count_dict(allsheet_dict, word_count_dict_All)
allsheet_dict = clean_dict(allsheet_dict)         
allsheet_dict = lower_dict(allsheet_dict)
#print allsheet_word_count
#print "\n"
#print allsheet_dict
#print "\n"



ezsheet_dict = extra_clean_dict(ezsheet_dict)
ezsheet_dict = clean_dict(ezsheet_dict)
ezsheet_dict = lower_dict(ezsheet_dict)
#print ezsheet_dict

##dictionary cleans working correctly check
#count = 0
#for word in allsheet_word_count:
#    for key in allsheet_dict:
#        if word == key:
#            count += 1
#            
#print count #gave 12(out of 13 categories)! \
#(which is what we want because we took out 'Total Words' key)