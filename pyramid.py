print("Enter a number:")
num = input()
num = int(num)

def print_triangle(stars):
	for x in range(1, stars + 1): # floor
		for j in range(stars - x): # J = 1
			print(" ", end='')
		for i in range(1, x + 1):
			print("* ", end='')
		print(" ")
		
print_triangle(num)