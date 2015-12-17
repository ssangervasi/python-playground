'''\
puzzle to solve from: 
	http://www.gchq.gov.uk/press_and_media/news_and_features/Pages/Directors-Christmas-puzzle-2015.aspx

Description of puzzle:

	In this type of grid-shading puzzle, each square is either black or white. Some of the black squares have already been filled in for you.

	Each row or column is labelled with a string of numbers. The numbers indicate the length of all consecutive runs of black squares, and are displayed in the order that the runs appear in that line. For example, a label "2 1 6" indicates sets of two, one and six black squares, each of which will have at least one white square separating them.
'''
import puzzle_classes as pzl

class GridPuzzle():
	"""Wrapper for puzzle data"""
	def __init__(self, patterns = None, grid = None):
		self.setGrid(grid or [[]])
		self.patterns = {
			"rows": patterns[0],
			"columns": patterns[0]
		}
		self.sequences = []
		self.active = 0
		self.offset = 0
		return

	def setGrid(self, grid):
		self.grid = grid
		self.width = len(self.grid)
		return self.grid
	
	def buildSequences(self):
		self.sequences = [None for i in range(self.width)]
		self.last = self.width - 1
		for rowIndex in range():
			initalState = self.grid[rowIndex]
			pattern = self.patterns['row'][rowIndex]
			self.sequences[self.width] = pzl.Sequence(pattern, row)

		return self.sequences


	def nextSolution(self):
		activeSeq = self.sequences[self.active]
		restarted = activeSeq.nextState()
		if not restarted:
			self.active = min(self.active + 1, self.last)

		else:
			self.active -= 1
					

	# def nextSolution(self):
	# 	activeSeq = self.sequences[self.active]
	# 	restarted = activeSeq.nextState()
	# 	if restarted:
	# 		self.active += 1
	# 		if self.active >= self.width:
	# 			self.offset += 1
	# 			self.active = self.offset
	# 			for offset in range(self.offset)
	# 				offsetSeq = self.sequences[offset]
	# 				offsetSeq.nextState()


	# End GridPuzzle
simpleData = [
	[
		[
			[1, 2],
			[1, 2, 1]
		],
		[
			[1],
			[2, 1]
		]
	],
	[
		[0 for i in range(7)] for i in range(7)
	]
]
simplePuzzle = GridPuzzle(simpleData[0], simpleData[1])
