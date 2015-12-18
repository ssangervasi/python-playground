import puzzle_classes as PzlClass
from util import PuzzleUtil as PzlUtil
import puzzle as Pzl

def main(args):
	print("Args: ", args)
	argSet = set(args)
	if '-t' in argSet or '--run-tests' in argSet: 
		runTests()
		print("Passed all tests.")

	solvePuzzle("simple")
	solvePuzzle("hard")
	return

def solvePuzzle(name):
	print("""
		Solving puzzle: {}
		=======================
		""".format(name))
	puzzle = Pzl.getPuzzle(name)
	soln = puzzle.solve()
	if soln:
		print(soln)
		PzlUtil.drawSolution(name + "-solution", soln)
	else:
		print("""
			NO SOLUTION
			""")
	print("""
		==========================
		""")


def runTests():
	testSequenceInit()
	testStateTransitions()
	return

def testSequenceInit():
	print('''
		Test sequence construction and validation.
		==========================================''')

	shouldBeTrue = [
		([], []),
		([1, 2], [0, 1, 0, 1, 1]),
		([3, 4, 1, 2], [1, 1, 1, 0, 0 , 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1])
	]
	shouldBeFalse =	[
		([1], []),
		([1, 2], [0, 1, 0, 1, 0]),
		([2, 4, 1, 2], [1, 1, 1, 0, 0 , 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1])
	]

	for test in shouldBeTrue:
		assert PzlUtil.matches(test[0], test[1])
		seq = PzlClass.Sequence(test[0], test[1], log = True)
		assert seq is not None
		assert seq.spreadGroups()
		startingState = PzlUtil.stateForGroups(seq.groups, length = seq.length)
		print(startingState)
		assert startingState is not None and len(startingState) == seq.length

	for test in shouldBeFalse:
		assert not PzlUtil.matches(test[0], test[1])
		assert PzlClass.Sequence(test[0], test[1], log = True) is not None
	
	return

def testStateTransitions():
	print('''
		Test transitions between sequence states.
		==========================================''')
	testData = [
		# (
		# 	[1 for i in range(2)],
		# 	[0 for i in range(7)]
		# ),
		# (
		# 	[1 for i in range(3)],
		# 	[0 for i in range(7)]
		# ),
		(
			[1, 2, 1],
			[0 for i in range(7)]
		),
		# (
		# 	[1 for i in range(2)],
		# 	[0 for i in range(7)]
		# ),
		# (
		# 	[1 for i in range(2)],
		# 	[0 for i in range(7)]
		# ),
	]

	for test in testData:
		runAllStates(PzlClass.Sequence(test[0], test[1], log = True))
	

def runAllStates(seq):
	maxStep = seq.length ** (seq.last + 1)
	step = 0
	states = [seq.state]
	while step < maxStep and (step == 0 or seq.stateIndex):
		step += 1
		seq.nextState()
		states.append(seq.state)

	PzlUtil.drawSolution('states-{}-{}'.format(seq.last, seq.length), states)
	return



if __name__ == "__main__":
	import sys
	main(sys.argv[0:-1])