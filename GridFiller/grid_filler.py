import puzzle_classes as pzl

def main(args):
	print("Args: ", args)
	testMethods()
	print("Passed all tests.")
	solution = solvePuzzle()
	print("Solved puzzle: ", solution)
	return

def solvePuzzle():
	return

def testMethods():
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
		startingState = pzl.Sequence.stateForGroups(seq.groups, length = seq.length)
		print(startingState)
		assert startingState is not None and len(startingState) == seq.length

	for test in shouldBeFalse:
		assert not pzl.PuzzleUtil.matches(test[0], test[1])
		assert pzl.Sequence(test[0], test[1]) is not None
	
	return

if __name__ == "__main__":
	import sys
	main(sys.argv[0:-1])

