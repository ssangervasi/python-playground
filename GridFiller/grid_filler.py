import puzzle_classes as pzl

def main(args):
	print("Args: ", args)
	runTests()
	print("Passed all tests.")
	solution = solvePuzzle()
	print("Solved puzzle: ", solution)
	return

def solvePuzzle():
	return

def runTests():
	testSequenceInit()
	testStateTransitions(2)
	testStateTransitions(3)
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
		assert pzl.PuzzleUtil.matches(test[0], test[1])
		seq = pzl.Sequence(test[0], test[1])
		assert seq is not None
		assert seq.spreadGroups()
		startingState = pzl.PuzzleUtil.stateForGroups(seq.groups, length = seq.length)
		print(startingState)
		assert startingState is not None and len(startingState) == seq.length

	for test in shouldBeFalse:
		assert not pzl.PuzzleUtil.matches(test[0], test[1])
		assert pzl.Sequence(test[0], test[1]) is not None
	
	return

def testStateTransitions(numGroups = 2, sequenceLength = 7):
	print('''
		Test transitions between sequence states.
		==========================================''')
	
	seq = pzl.Sequence([1 for i in range(numGroups)], [0 for i in range(sequenceLength)])
	maxStep = 100
	while maxStep and (maxStep == 100 or seq.stateIndex):
		maxStep -= 1
		seq.nextState()

	return

if __name__ == "__main__":
	import sys
	main(sys.argv[0:-1])

