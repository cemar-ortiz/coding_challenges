# Challenge description:
# Write a method to replace all spaces in a string with '%20'. You may assume that
# the string has sufficient space at the end to hold the additional characters, and
# that you are given the 'true' length of the string. (Note: if implementing in Java,
# please use a character array so that you can perform this operation in place)

# EXAMPLE
# Input: 'Mr John Smith    ', 13
# Output: 'Mr%20John%20Smith'

from functools import reduce

def urlify(input_string: str, true_len: int) -> str:
	# 1. Slice string up to its true length. Constant time
	true_string = input_string[:true_len]
	# 2. Switch blank spaces for '%20' in the string using a list comprehension. O(n)
	url_as_list = ['%20' if x==' ' else x for x in true_string]
	# 3. To show an alternative to using the str.join() method with reduce. O(n)
	# The reduce() function here, has the time complexity of a for cycle
	# https://docs.python.org/3/library/functools.html#functools.reduce
	url_as_str = reduce(lambda a,b: a+b, url_as_list)
	# Total complexity -> O(n) + O(n) = O(2n) = O(n)
	return url_as_str 


if __name__ == '__main__':
	test = 'This is a test my friend    '
	test_len = 24
	ans = urlify(test, test_len)
	print(test, ans, sep='/urlified: ')
	
	test = 'Mr John Smith    '
	test_len = 13
	ans = urlify(test, test_len)
	print(test, ans, sep='/urlified: ')
	
