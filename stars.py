print("Enter a number:")
num = input()
num = int(num)

def print_star(st):
	x = 1 
	while x <= st:
		print("*", end='')
		x += 1


print_star(num)