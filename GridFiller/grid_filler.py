import puzzle_classes as pzl
from PIL import Image, ImageDraw

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
		runAllStates(pzl.Sequence(test[0], test[1]))
	

def runAllStates(seq):
	maxStep = seq.length ** (seq.last + 1)
	step = 0
	states = [seq.state]
	while step < maxStep and (step == 0 or seq.stateIndex):
		step += 1
		seq.nextState()
		states.append(seq.state.copy())

	drawSolution('states-{}-{}'.format(seq.last, seq.length), states)
	return


def drawSolution(solutionName, states):
	soln = Image.new("RGB", (len(states[0]), len(states)), (255,255,255))
	draw = ImageDraw.Draw(soln)
	for row in range(len(states)):
		for col in range(len(states[0])):
			if states[row][col]:
				draw.point((col, row), (0,0,0))

	soln.save('solutions/' + solutionName + '.gif')
	return soln


if __name__ == "__main__":
	import sys
	main(sys.argv[0:-1])

