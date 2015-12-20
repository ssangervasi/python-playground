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
	fileName = 'puzzles/{}.json'.format(puzzleName)
	return readPuzzle(fileName)

def readPuzzle(fileName):
	try:
		infile = open(fileName)
	except:
		print("Could not read puzzle -- No such file: '{}'".format(fileName))
		return

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