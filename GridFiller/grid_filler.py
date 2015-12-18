import puzzle_classes as PzlClass
import puzzle as Pzl
from PIL import Image, ImageDraw

def main(args):
	print("Args: ", args)
	argSet = set(args)
	if '-t' in argSet or '--run-tests' in argSet: 
		runTests()
		print("Passed all tests.")

	solveSimplePuzzle()
	solveHardPuzzle()
	return

def solveSimplePuzzle():
	print("""
		Solving a simple puzzle
		=======================
		""")
	simplePattern =[
		[
			[1, 1],
			[1],
			[1, 1]
		],
		[
			[1, 1],
			[1],
			[1, 1]
		]
	]		
	simpleGrid = [
		[0 for i in range(3)] for i in range(3)
	]
	simplePuzzle = Pzl.GridPuzzle(simplePattern, simpleGrid)
	soln = simplePuzzle.solve()
	if soln:
		print(soln)
		drawSolution("simple-solution", soln)
	else:
		print("""
			NO SOLUTION
			""")
	print("""
		==========================
		""")

def solveHardPuzzle():
	print("""
		Solving a hard puzzle
		The output 'hard-solution.gif' should match 'hard-example.gif'
		=======================
		""")
	simplePattern =[
		[
			[1, 1],
			[1, 1],
			[1, 1, 1],
			[1, 1],
			[1, 1]
		],
		[
			[1, 1, 1],
			[1, 1],
			[1],
			[1],
			[3, 1]
		]
	]		
	simpleGrid = [
		[0 for i in range(5)] for i in range(5)
	]
	simpleGrid[0][0] = 1
	simpleGrid[2][2] = 1
	simplePuzzle = Pzl.GridPuzzle(simplePattern, simpleGrid)
	soln = simplePuzzle.solve()
	if soln:
		print(soln)
		drawSolution("hard-solution", soln)
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
		assert PzlClass.PuzzleUtil.matches(test[0], test[1])
		seq = PzlClass.Sequence(test[0], test[1], log = True)
		assert seq is not None
		assert seq.spreadGroups()
		startingState = PzlClass.PuzzleUtil.stateForGroups(seq.groups, length = seq.length)
		print(startingState)
		assert startingState is not None and len(startingState) == seq.length

	for test in shouldBeFalse:
		assert not PzlClass.PuzzleUtil.matches(test[0], test[1])
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

	drawSolution('states-{}-{}'.format(seq.last, seq.length), states)
	return


def drawSolution(solutionName, states):
	height = len(states)
	width = len(states[0])
	sqpx = 25
	soln = Image.new("RGB", (width * sqpx + 1, height * sqpx + 1), (255,255,255))
	draw = ImageDraw.Draw(soln)
	for row in range(height):
		
		for col in range(width):
			x = col * sqpx 
			y = row * sqpx
			fill = (255,255,255)
			if states[row][col]:
				fill = (0,0,0)
			draw.rectangle([x, y, x + sqpx, y + sqpx], fill, (211,226,0))

	soln.save('solutions/' + solutionName + '.gif')
	return soln


if __name__ == "__main__":
	import sys
	main(sys.argv[0:-1])

