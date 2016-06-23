Project:
Collection of different code:

-read an excel book 
	-needs to be revised 
		-hard-coded to my computer’s directories
		-works in excel to create separate sheets from book to read sheets as 			dictionaries.(runtime is ~ 2 sec)
	-columns in WordCategories are subclasses of other classes (ex: Nouns > 			Animals)

-calculate average difficulty of words in books
	- base simple code needs to be revised
		- words not in All or Easy list that may not be exceptionally hard
			- numbers (1,2,3,4…) and letters (a,b,c,d…)
			- names
			- SOLUTION: use wordnet(not tried)

- import tokenize, pos tag, and lemmatize txt files
	- need to batch import
	- error in using batch_pos_tag
	
	
Overall Problems:
-lengthy code with long run time
-many hard-coded sections
-not very organized
	-use classes instead of purely functions
	-shorten code using list comprehensions
	-
