# Given two strings, write a method to decide if one is a permutation
# of the other

# Assumption, both strings given are of the same length

string_a = 'aarbol'
string_b = 'bborla'

def is_permutation(string_a: str, string_b: str):
	
	# Esto guarda un conjunto de los caracteres sin repetir
	key_set = set(string_a)
	# Lo convierto a una lista, porque el tipo set no es indexable
	key_list = list(key_set)
	
	# Construyo un diccionario donde le asigno un valor unico y mayor de 0 a cada letra
	key_dict = {key_list[i]: i+1 for i in range(0, len(key_list))}
	
	# Traduzco cada letra a un numero por string
	list_a = [key_dict[i] for i in string_a]
	# En el caso del string_b, asigno un 0 a letras que no están en el dictionario
	list_b = [key_dict[i] if i in key_dict.keys() else 0 for i in string_b] 
	
	# Retorno la comparacion de la suma de los valores
	return string_a, list_a, string_b, list_b, sum(list_a) == sum(list_b) 

if __name__ == '__main__':
	print(is_permutation(string_a, string_b))
	
