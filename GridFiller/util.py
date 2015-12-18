from PIL import Image, ImageDraw
import progressbar as Pbar
import math

class PuzzleUtil:
	'''Static methods for solving the puzzle'''

	def zeroes(length = 0):
		return [0 for i in range(length)]

	def stateForGroups(groups, length = 0, state = None):
		if not state:
			state = PuzzleUtil.zeroes(length)
		else:
			length = len(state)

		for group in groups:
			for bit in group:
				if bit >= length:
					return None
				state[bit] = 1

		return state
		
	def matches(pattern, sequence):
		'''Static helper checks whether a pattern is matched by a particular sequence.'''
		nextGroup = 0
		groupLen = 0
		for entryIndex in range(len(sequence)):
			entry = sequence[entryIndex]
			isFilled = (entry > 0)
			groupLen += isFilled
			# Check for group match if the group just ended or the end of the list is reached
			if groupLen > 0 and (not isFilled or entryIndex == len(sequence) - 1):
				if (len(pattern) - 1 < nextGroup) or groupLen != pattern[nextGroup]:
					return False

				groupLen = 0
				nextGroup += 1

		# Ensure last-found group was the last pattern
		return nextGroup == len(pattern)


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

	# End PuzzleUtil
	
class LogBar:
	"""Progress bar that updates on log scale"""

	def __init__(self, maxValue, factor = 10.0):
		self.factor = factor if isinstance(factor, float) and factor > 1 else 10.0
		maxRefactored = self.refactor(maxValue)
		self.bar = Pbar.ProgressBar(max_value = maxRefactored, widgets = [Pbar.Percentage(), Pbar.Bar(), Pbar.ETA()])
		return
	
	def refactor(self, val):
		if not val:
			return
		return math.log(float(val), self.factor)

	def start(self, updateVal = None):
		return self.bar.start(self.refactor(updateVal))

	def finish(self):
		return self.bar.finish()

	def update(self, updateVal):
		return self.bar.update(self.refactor(updateVal))


def loopTest(breadth, depth):
	results = []
	arr = [0 for i in range(breadth)]
	active = 0
	back = 0
	while active > -1:
		if active >= breadth:
			active -= 1
			back = 1
			continue

		arr[active] += back
		if arr[active] == depth:
			arr[active] = 0
			active -= 1
			back = 1
			continue
		
		active += 1
		back = 0
		results.append(''.join(str(max(val, 0)) for val in arr))

	return results

def recursionTest(breadth, depth):
	results = []
	recursionHelper(0, depth, [0 for i in range(breadth)], results)
	return results

def recursionHelper(index, depth, arr, results):
	if index >= len(arr):
		return
	for myDepth in range(depth):
		# nextArr = arr.copy()
		nextArr = arr
		nextArr[index] = myDepth
		results.append(''.join(str(val) for val in nextArr))
		recursionHelper(index + 1, depth, nextArr, results)

def testIterators():
	m = 4
	n = 2
	loopRes = loopTest(m, n)
	print(loopRes)
	print("Actual", len(loopRes))
	print("Unique", len(set(loopRes)))

	recRes = recursionTest(m, n)
	print(recRes)
	print("Actual", len(recRes))
	print("Unique", len(set(recRes)))

	print("Diff?", set(recRes) - set(loopRes))
