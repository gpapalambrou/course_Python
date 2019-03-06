# open a file
filename = input('Enter file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
	print(eachLine,)
fobj.close()
