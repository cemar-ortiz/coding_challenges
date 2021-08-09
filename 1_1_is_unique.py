from functools import reduce


string_1 = 'aabcd'
string_2 = 'abcd'
string_3 = 'abcdddd'

from datetime import datetime

# Pasando *args y **kwargs puedo hacer mas flexible
# mi decorador al hacerlo capaz de recibir argumentos
def execution_time(func):
	def wrapper(*args, **kwargs):
		init_time = datetime.now()
		func(*args, **kwargs)
		final_time = datetime.now()
		time_elapsed  = final_time - init_time
		print('Pasaron: ' + str(time_elapsed.total_seconds()) + 'segundos')
	return wrapper

@execution_time
def is_unique(string: str) -> bool:
	# 1. Por cada caracter de string
	for i in string:
		# 2. La funcion map() retorna un iterador, evitando guardar
		# una lista, donde el iterador compara cada letra con el
		# indice actual
		mapped = map(lambda a: a==i, string)
		
		# 3. Paso el iterador a una funcion que suma sus valores
		reduced =  reduce(lambda a,b: a+b, mapped)
		
		# 4.1 Si la suma es mayor a 1, significa que hay repetidos
		if reduced > 1:
			return print(string, 'Not all unique')
	
	# 4.2 Si la suma es mayor a 2, significa que todos son unicos
	return print(string, 'all unique')
	

if __name__ == '__main__':
	is_unique(string_1)
	is_unique(string_2)
	is_unique(string_3)

