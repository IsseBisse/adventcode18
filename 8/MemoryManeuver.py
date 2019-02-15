def parseInput(filename):
	f = open(filename, "r")

	input = f.read()
	return input

'''
Part 1
'''
def partOne():
	fileData = parseInput("testInput.txt")
	print(fileData)

'''
Part 2
'''


'''
Main
'''
if __name__ == '__main__':
	partOne()