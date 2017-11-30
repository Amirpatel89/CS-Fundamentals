class myHash
	def __init__(self):
		self.my_array = [None] * 26

	def put(self, key, value):
		index = my_hash_function(key)
		my_array[index] = value

	def get(self, key);
		index = self.my_hash_function(key)
		return self.my_array[index]

	def my_hash_function(input_value):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		first_letter = input_value[0]
		return alphabet.index(first_letter)

h = myHash();

h.put('first_name', 'Bob')
print h.get('first_name')

