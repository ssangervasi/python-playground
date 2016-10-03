from ..solver.solver import Solver

def sleep_count(n):
	INSOMNIA = 'INSOMNIA'
	if n == 0:
		return INSOMNIA
	is_seen = [False for i in range(10)]
	i = 0
	while True:
		i += 1
		current_multiple = i*n
		for digit in str(current_multiple):
			is_seen[int(digit)] = True
		if all(is_seen):
			return current_multiple
			# return '{} ({})'.format(current_multiple, i)
		
		if i == 10**5:
			print('Might be exploading!')


def pancake_flipper(stack):
	if len(stack) < 1:
		return 0
	flips = 0
	current = stack[0]
	for pancake in stack[1:]:
		if pancake != current:
			flips += 1
			current = pancake
	if current == '-':
		flips += 1
	return flips

which = input('Which solutions?').lower()

if 'a' in which:
	sleep_solver = Solver(sleep_count, parser=int)
	sleep_solver.solve_file('primes.txt')
	sleep_solver.solve_file('A-small-practice.in', 'A.out')
	sleep_solver.solve_file('A-large-practice.in', 'A-large.out')

if 'b' in which:
	pancake_solver = Solver(pancake_flipper)
	pancake_solver.solve_file('B-small-practice.in', 'B-small.out')