# break example
num=input('give an integer number:')
num=int(num)	# convert to integer
count = num / 2
while count > 0:
	if num % count == 0:
		print(count, 'is the largest factor of', num)
		break
	count -= 1
