# Implement an algorithm to determine if a string has all unique characters. 

def task(string: str) -> (str, str):
	
	# 1 Pass input string into a list
	str_list = list(string) # O(n)
	
	# 2 Define a function that removes all instances of an item from a list
	#   and checks its length before and after the operation.
	def remove_task(in_list):
		len_before = len(in_list)
		i = in_list[0]
		str_list = [char for char in in_list if char != i] # O(n)
		len_after = len(str_list)
		
		# If the difference is bigger than -1, then repeated characters were removed 
		diff = len_after - len_before
		if diff < -1:
			ans = 'not unique'
			return ans
		# If a total length of 0 has been reached, no repeated characters were found
		if len_after == 0:
			ans = 'unique'
			return ans
			
		# If length is still not 0, call remove_task(str_list) again 
		ans = remove_task(str_list)
		return ans
	
	# Recursion start. It will be called a max of n times
	ans = remove_task(str_list)
	
	# All operations not specified otherwise are estimated as constant time
	# Estimated total time complexity of O(n²)
	return (string, ans)
