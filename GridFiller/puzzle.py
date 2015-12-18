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
			"columns": patterns[1]
		}
		self.sequences = []
		self.active = 0
		self.increment = False
		return

	def setGrid(self, grid):
		self.grid = grid
		self.width = len(self.grid)
		self.height = len(self.grid[0])
		return self.grid
	
	def buildSequences(self):
		self.sequences = [None for i in range(self.width)]
		for rowIndex in range(self.width):
			initalState = self.grid[rowIndex]
			pattern = self.patterns["rows"][rowIndex]
			self.sequences[rowIndex] = pzl.Sequence(pattern, initalState)

		return self.sequences

	def solve(self, maxStep = 100000):
		stepsRemaining = 0
		self.buildSequences()
		exhausted = False
		while stepsRemaining < maxStep and not exhausted and not self.isSolved():
			exhausted = self.nextSolution()

		if stepsRemaining == maxStep:
			print("No solution amongst first {} combinations".format(maxStep))

		elif exhausted:
			print("Unsolvable")

		else:
			return self.getSolutionGrid()

	def getSolutionGrid(self):
		return [seq.state for seq in self.sequences]

	def isSolved(self):
		grid = self.getSolutionGrid()
		for column in range(self.height):
			state = [grid[row][column] for row in range(self.height)]
			pattern = self.patterns['columns'][column]
			if not pzl.PuzzleUtil.matches(pattern, state):
				return False

		return True

	def nextSolution(self):
		"""
		Step to the next solution state.
		Currently innefficient and will not ignore duplicate states.
		Returns True if all states have been explored, else False.
		"""
		# Check whether last sequence has been reached
		if self.active >= self.width:
			self.active -= 1
			self.increment = True
			return False

		# Check whether the current sequence should be stepped through
		restarted = False
		if self.increment:
			activeSeq = self.sequences[self.active]
			restarted = activeSeq.nextState()
		
		# If the current sequence did a full loop, step backwards
		if restarted:
			self.active -= 1
			self.increment = True
			return self.active < 0

		# Usually just step forwards
		self.active += 1
		self.increment = False
		return False

	# End GridPuzzle
