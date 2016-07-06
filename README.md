Project:
-tokenize, pos_tag, and lemmatize words from children's books
-record the average difficulty of the words in each book

Run book_values.py


File_functions:
-book_values: contains calculate_book_values function
	-uses inputs from modify_dictionary_from_excel, importing_txt_files,*_modify
	-contains code for importing excel files
	-print statements at end of script for each book  print:
		-title
		-total points awarded
		-total words(not including stopwords)		
		-total words(including stopwords)
		-difficulty (total points awarded / total words	(not including stopwords))
		-difficulty (total points awarded/ total words (including stopwords)) 

resources:
contains *.xlsx files, and StoryCorpus

modify_dictionary_from_excel.py: converts excel sheets to dictionaries and contains functions to find non-alphanumeric words and create custom_stopwords list

importing_txt_files.py: tokenize, pos_tag, and lemmatize words from StoryCorpus files

fixing_strings (final_words_modifier): concatenates halves of contractions into wholes

punctuation_modify (final_words_modifier): removes punctuation from long strings, removes short strings with punctuation

numeral_word_modify (final_words_modifier): changes arabic numeral strings to their equivalent word

propnoun_modify (final_words_modifier): removes proper nouns from the final words list

stopwords_modify (final_words_modifier): removes stopwords from the final words list

find_propernouns: NOT USED IN BOOK_VALUES. finds propernouns

word_search: NOT USED IN BOOK_VALUES. contains framework for searching for words from books in All and Easy dictionaries by mapping pos_tag to specific keys
	
