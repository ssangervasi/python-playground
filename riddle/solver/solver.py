
class Solver(object):
	def __init__(self, solver, parser=str.strip):
		self.solver = solver
		self.parser = parser

	def solve(self, cases, case_count=1):
		out = []
		for case in cases:
			solution = self.solver(case)
			line = 'Case #{}: {}\n'.format(case_count, solution)
			out.append(line)
			case_count += 1
		return out

	def solve_file(self, test_file, out_file):
		with open(out_file, 'w') as out:
			with open(test_file) as test:
				test_count = int(test.readline())
				chunk_size = 100
				cases = []
				case_count = 1
				for line in test:
					cases.append(self.parser(line))
					if len(cases) == chunk_size:
						solution = self.solve(cases, case_count)
						out.writelines(solution)
						case_count += chunk_size
						cases = []
				if len(cases) > 0:
						solution = self.solve(cases, case_count)
						out.writelines(solution)
						case_count += chunk_size
