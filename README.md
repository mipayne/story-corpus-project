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
	
