from challenges import one_away

task = one_away.task

# content of test_class.py
class TestClass:
	def test_one(self):
		# Case when only a remove is necessary, returns True
		assert task('pale', 'ple') == True
        
	def test_two(self):
		# Case when only an insert is necessary, returns True
		assert task('pale', 'pales') == True
	
	def test_three(self):
		# Case when only a replace is necessary, returns True
		assert task('pale', 'bale') == True
	
	def test_four(self):
		# Case when two replaces are necessary, returns False
		assert task('pale', 'bake') == False
	
	def test_five(self):
		# Case when zero edits are necessary, returns True
		assert task('pale', 'pale') == True
