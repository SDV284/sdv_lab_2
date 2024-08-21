def func_2(x, y):
	if x > y:
		return "Error: x cannot be greater than y"
	s = 0
	for i in range(int(x), int(y)+1): 
		if i % 2 == 0: 
			s += i
	return s