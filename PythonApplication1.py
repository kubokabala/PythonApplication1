import math
print("Hi there")

N = 365
R = input("кол-во человек bg: ")
R = int(R)

R1 = input("кол-во человек end: ")
R1 = int(R1)

A = math.factorial(N)

while R <= R1:
	B = math.factorial(N - R)
	print(1 - A / (B * (N ** R)))
	R += 1