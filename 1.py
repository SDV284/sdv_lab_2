from math import sin

def func_1(x):
	return (1-2*pow(sin(int(x)),2)/(1+pow(sin(int(x)),2)))

def func_2(x, y):
	if x > y:
		return "Error: x cannot be greater than y"
	s = 0
	for i in range(int(x), int(y)+1): 
		if i % 2 == 0: 
			s += i
	return s

print("Result: ", func_1(input("Function 1. \nEnter x: ")))
print("Result: ", func_2(input("Function 2. \nEnter x: "), input("Enter y: ")))