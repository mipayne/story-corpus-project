Project:
-tokenize, pos_tag, and lemmatize words from children's books
-record the average difficulty of the words in each book

File_functions:
-book_values: contains calculate_book_values function
	-uses inputs from modify_dictionary_from_excel, importing_txt_files,
		fixing_strings, stopwords_modify, punctuation_modify, and
		numeral_word_modify
	-contains code for importing excel files 
	-non_function code outputs value_dict, a dictionary of book filenames
		and a list [tot_word_value, avg_book_difficulty] 

-modify_dictionary_from_excel: converts excel sheets to dictionaries
	- contains functions:
		-create_dictionary
			-creates dictionaries from imported excel sheets
		-make_word_count_dict
			-records category word counts from All sheet
		-extra_clean_dict
			-removes blank keys
		-clean_dict
			-removes blank elements in key values
		-lower_dict
			-makes elements lowercase and ascii
		-modify_dictionary
			-calls extra_clean, clean_dict, and lower_dict
		-find_non_alnum
			-finds non-alphanumeric words including contractions
			-basis for fixing_strings modifier
		-create_custom_stopword_list
			-imports stopwords from nltk.corpus
			-removes words found in ALL excel sheet
-importing_txt_files:
	-contains functions:
		-get_wordnet_pos
			-converts treebank_tag to simple wordnet tag
		-import_txt
			-tokenize, pos_tag, and lemmatize words from files in
				StoryCorpus
			-imports txt files and nltk
			-does not preserve original pos_tag
				-contains comments to begin to preserve
-fixing_strings (final_words modifier):
	-contains functions:
		-modify_words1
			-concatenates halves of contractions into 1 whole word
			-removes halves from and adds wholes to final_words list-stopwords_modify (final_words modifier):
	-contains functions:
		-modify_words2
			- removes stopwords from final_words list
-punctuation_modify (final_words modifier):
	-contains functions:
		-modify_words3
			-removes punctuation from long strings, removes short
				strings with punctuation
-numeral_word_modify (final_words modifier):
-word_search:
	-NOT USED IN CURRENT BOOK_VALUES CODE
	-contains framework for searching for words from books in All and Easy
		dictionaries by mapping pos_tag to specific keys
-resources
	-contains:
		-converted/StoryCorpus
		-StoryCorpus
		-xlsx files
