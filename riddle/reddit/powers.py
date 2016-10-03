from ..solver.solver import Solver


cases = [
	(216, 512),
	(125, 343),
	(64, 216),
	(27, 125),
	(8, 64),
]

def solve_powers(case):
	def find_power(number):
		base, power = 2, 2
		while True:
			result = base**power
			if result == number:
				break
			elif result > number:
				base += 1
				power = 2
			else:
				power += 1
		return (number, base, power)
	return tuple(map(find_power, case))

power_solver = Solver(solve_powers)
for solution in power_solver.solve(cases):
	print(solution)
