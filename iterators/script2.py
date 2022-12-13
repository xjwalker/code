# A Python program to demonstrate working of Generators
def Reverse(data):
	# this is like counting from 100 to 1 by taking one(-1)
	# step backward.
	for index in range(len(data)-1, -1, -1):
		yield data[index]

def Main():
	rev = Reverse('Harssh')
	for char in rev:
		print(char)
	data ='Harssh'
	# start, stop, step.
	print(list(data[i] for i in range(len(data)-1, -1, -1)))

if __name__=="__main__":
	Main()
