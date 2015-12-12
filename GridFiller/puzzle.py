'''\
puzzle to solve from: 
	http://www.gchq.gov.uk/press_and_media/news_and_features/Pages/Directors-Christmas-puzzle-2015.aspx

Description of puzzle:

	In this type of grid-shading puzzle, each square is either black or white. Some of the black squares have already been filled in for you.

	Each row or column is labelled with a string of numbers. The numbers indicate the length of all consecutive runs of black squares, and are displayed in the order that the runs appear in that line. For example, a label "2 1 6" indicates sets of two, one and six black squares, each of which will have at least one white square separating them.
'''

class GridPuzzle():
	"""Wrapper for puzzle data"""
	def __init__(self, grid = None, groups = None, rowLen = 0):
		self.grid =  [[0 for i in range(rowLen)] for j in range(rowLen)]
		self.groups =  {
			"rows": [] for i in range(rowLen),
			"columns": [] for i in range(rowLen)
		}
		return
	
	# End GridPuzzle

simplePuzzle = GridPuzzle(5)
mainPuzzle = GridPuzzle(rowLen = 25)
