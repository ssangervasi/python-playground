'''\
puzzle to solve from: 
	http://www.gchq.gov.uk/press_and_media/news_and_features/Pages/Directors-Christmas-puzzle-2015.aspx

Description of puzzle:

	In this type of grid-shading puzzle, each square is either black or white. Some of the black squares have already been filled in for you.

	Each row or column is labelled with a string of numbers. The numbers indicate the length of all consecutive runs of black squares, and are displayed in the order that the runs appear in that line. For example, a label "2 1 6" indicates sets of two, one and six black squares, each of which will have at least one white square separating them.
'''
import puzzle_classes as PzlClass
import json

def getPuzzle(puzzleName = "simple"):
	if puzzleName == "simple":
		return getSimpleGridPuzzle()

	elif puzzleName == "hard":
		return getHardGridPuzzle()

	elif puzzleName == "large":
		return getLargeGridPuzzle()

def getSimpleGridPuzzle():
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
	simplePuzzle = PzlClass.GridPuzzle(simplePattern, simpleGrid)
	return simplePuzzle

def getHardGridPuzzle():
	hardPattern =[
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
	hardGrid = [
		[0 for i in range(5)] for i in range(5)
	]
	hardGrid[0][0] = 1
	hardGrid[2][2] = 1
	hardPuzzle = PzlClass.GridPuzzle(hardPattern, hardGrid)
	return hardPuzzle

def getLargeGridPuzzle():
	return readPuzzle('puzzles/large.json')

def readPuzzle(fileName):
	infile = open(fileName)
	# Just reading whole text blob for now
	fileText = infile.read()
	infile.close()
	asJson = json.loads(fileText)
	gridInfo = asJson["grid"]
	grid = [
		[
			0 for column in range(gridInfo["height"])
		] for row in range(gridInfo["width"])
	]
	for filled in gridInfo["prefilled"]:
		grid[filled[1]][filled[0]] = 1

	return PzlClass.GridPuzzle(asJson["patterns"], grid)

def testSolve():
	large = getLargeGridPuzzle()
	large.buildSequences()
	return large