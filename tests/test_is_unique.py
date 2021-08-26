from challenges import is_unique

task = is_unique.task

string_1 = 'aabcd'
string_2 = 'abcd'
string_3 = 'abcdddd'
string_4 = 'murcielago'
string_5 = 'mi nombre es yoshikage kira, quiero llevar una vida tranquila'

out_a = 'unique'
out_b = 'not unique'


# content of test_class.py
class TestClass:
	def test_one(self):
		assert task(string_1) == (string_1, out_b)
		
  
	def test_two(self):
		assert task(string_2) == (string_2, out_a)
		
		
	def test_three(self):
		assert task(string_3) == (string_3, out_b)
		
		
	def test_four(self):
		assert task(string_4) == (string_4, out_a)
		
		
	def test_five(self):
		assert task(string_5) == (string_5, out_b)
		
