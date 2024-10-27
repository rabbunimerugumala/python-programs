



import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write(input("Enter The List Values: "))

	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			data = f.readlines()
			for line in data:
				word = line.split()
				print(word)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(input("Enter The Elements To Add: "))
	except IOError:
		print("Error: could not append to file " + filename)



def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "todo.txt"

	# create_file(filename)
	# read_file(filename)
	# append_file(filename,text="")
	# delete_file(filename)
