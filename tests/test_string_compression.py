from challenges import string_compression

task = string_compression.task

# content of test_class.py
class TestClass:
	def test_one(self):
		# Case when compression can return a shorter string
		assert task('aabcccccaaa') == 'a2b1c5a3'
        
	def test_two(self):
		# Case when compression would return a longer string should return input as is
		assert task('abcdefg') == 'abcdefg' 
