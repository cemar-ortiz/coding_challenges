# Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words. You can ignore casing and non-letter characters.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: 'taco cat', 'atco cta', etc.)

def is_palindrome_permutation(input_string: str):
	# 1. Turn input into lowercase -> Constant time
	new_string = input_string.lower()
	
	# 2. Remove blank spaces in the string -> Constant time
	new_string = new_string.replace(' ', '')
	
	# 3. Count occurrence of each letter in the string
	# 3.1 Get a list of non-repeated letters -> Constant time
	letters = list(set(new_string))
	
	# 3.2 Count the occurrence of each letter in new_string -> O(n*n)
	modulus = [] 
	for i in letters:
		count = 0
		for j in new_string:
			if i == j:
				count+=1
		# 3.3 Get the modulus of 2 of each count -> Constant time
		modulus.append(count%2)
	
	# 3.4 Sum the list of modulus -> O(n)
	modulus_sum = sum(modulus)
	
	# 3.5 Evaluate if modulus_sum is <=1
	ans = modulus_sum <= 1
	
	# Total estimated time complexity -> O(n*n)
	return ans 
	
	

if __name__ == '__main__':
	test = 'Tact Coa'
	ans = is_palindrome_permutation(test)
	print(test, ans, sep=' ')
	
	test = 'Barbolabol'
	ans = is_palindrome_permutation(test)
	print(test, ans, sep=' ')
	
	test = 'Anita lava la tina'
	ans = is_palindrome_permutation(test)
	print(test, ans, sep=' ')
	
	test = 'Anita esta huerfanita pobre anita'
	ans = is_palindrome_permutation(test)
	print(test, ans, sep=' ')
