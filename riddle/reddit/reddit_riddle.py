# from ..solver import Solver
# from riddle.solver import solver


nums = [
          0,
         10,
       1110,
       3110,
     132110,
   31131210,
   23411210,
]

# pairs = [(nums[i], nums[i+1])
#          for i in range(len(nums)-1)]
# print(pairs)
# diffs = list(map(lambda p: p[1] - p[0], pairs))
# print(*diffs, sep='\n')

def next_number(number):
	digits = list(map(int, [n for n in str(number)]))
	new_digits = []
	seen = set()
	for digit in digits:
		if digit in seen:
			continue
		seen.add(digit)
		matches = len([other for other in digits
									 if other == digit])
		new_digits.append(matches)
		new_digits.append(digit)
	return int(''.join(map(str, new_digits)))

for i, n in enumerate(nums):
	if i == 0:
		continue
	print('{}\tvs\t{}'.format(n, next_number(nums[i-1])))

s = 0
for i in range(100):
	s2 = next_number(s)
	print(s2)
	if s2 == s:
		print(i)
		break
	s = s2