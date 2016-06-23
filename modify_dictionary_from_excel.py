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
split_a_book('/Users/Madelyn/Desktop/UROP/py_codes/WordCategories.xlsx', 'output.xlsx')
import glob
outputfiles = glob.glob('*_output.xlsx')#splits book to be single sheets
for file in sorted(outputfiles):
    sheet_list.append(file)#adds each new sheet to a list
##print("--- %s seconds ---" % (time.time() - start_time))
    
print sheet_list
print sheet_list[0]
if sheet_list[0] == 'All_output.xlsx':#makes sure it's the right sheet (not necessary)
    #gets excel sheet and makes into a dictionary (keys= row_1)
    sheet1 = pyexcel.get_sheet(file_name = sheet_list[0], name_columns_by_row=0)
    sheet1_od = sheet1.to_dict() 
    sheet1_dict = dict(sheet1_od)
if sheet_list[1] == 'Easy_output.xlsx':
    sheet2 = pyexcel.get_sheet(file_name = sheet_list[1], name_columns_by_row=0)
    sheet2_dict = dict(sheet2.to_dict())
else:
    print "You don't have the appropriate sheet names"
    
#print sheet1_dict
#print sheet2_dict


#sheet1_od = sheet.to_dict()
#sheet1_dict = dict(sheet1_od)
#print sheet1_dict
#sheet2_od = dict(sheet.to_dict())
#book[sheet_index][row, column]


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
            x = x.lower()
            y.append(x)
        my_dict[key] = y
    return my_dict

sheet1_dict = extra_clean_dict(sheet1_dict)
sheet1_word_count = make_word_count_dict(sheet1_dict, word_count_dict_All)
print sheet1_word_count
print "\n"
sheet1_dict = clean_dict(sheet1_dict)
#print sheet1_dict

print "\n"

sheet2_dict = extra_clean_dict(sheet2_dict)
sheet2_dict = clean_dict(sheet2_dict)
print sheet2_dict
sheet2_dict = lower_dict(sheet2_dict)
print sheet2_dict

##dictionary cleans working correctly check
#count = 0
#for word in sheet1_word_count:
#    for key in sheet1_dict:
#        if word == key:
#            count += 1
#            
#print count #gave 12! ( which is what we want because we took out 'Total Words' key)