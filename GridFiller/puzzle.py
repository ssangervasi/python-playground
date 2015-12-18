'''\
puzzle to solve from: 
	http://www.gchq.gov.uk/press_and_media/news_and_features/Pages/Directors-Christmas-puzzle-2015.aspx

Description of puzzle:

	In this type of grid-shading puzzle, each square is either black or white. Some of the black squares have already been filled in for you.

	Each row or column is labelled with a string of numbers. The numbers indicate the length of all consecutive runs of black squares, and are displayed in the order that the runs appear in that line. For example, a label "2 1 6" indicates sets of two, one and six black squares, each of which will have at least one white square separating them.
'''
import puzzle_classes as PzlClass

def getPuzzle(puzzleName = "simple"):
	if puzzleName == "simple":
		return getSimpleGridPuzzle()

	elif puzzleName == "hard":
		return getHardGridPuzzle()

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