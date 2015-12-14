
class Sequence:
	'''Wraps a sequence of 0's and 1's and maintains the state of possible sequences.'''

	def __init__(self, pattern, state):
		self.length = len(state)
		self.pattern = [int(groupLen) for groupLen in pattern]
		self.initialState = [int(bit) for bit in state]
		self.prefilled = [index for index in range(self.length) if self.initialState[index] > 0 ]
		self.groups = [Group(nextLen) for nextLen in pattern]
		self.invalidStates = set()
		return

	def spreadGroups(self):
		nextStart = 0
		lastGroup = None
		for group in self.groups:
			group.setStart(nextStart)
			nextStart = group.end + 2
			lastGroup = group

		return (not lastGroup) or lastGroup.end < self.length

	def nextState(self):
		if not self.state:
			self.stateIndex = 0
			self.spreadGroups()
			self.state = PuzzleUtil.stateForGroups(self.groups, self.length)
			self.activeGroup = len(self.groups) - 1
			return self.state

		self.stateIndex += 1
		self.shiftGroups()
		while self.stateIndex in self.invalidStates:
			self.stateIndex += 1
			self.shiftGroups()

		# Default sequence has some bits filled
		newState = self.initialState.copy()
		PuzzleUtil.stateForGroups(self.groups, state = newState)
		if PuzzleUtil.matches(self.pattern, newState):
			self.state = newState
		else:
			self.invalidStates.add(self.stateIndex)
			self.nextState()

		return self.state

	def shiftGroups(self):
		groupToShift = self.groups[self.activeGroup]
		groupToShift.shift()
		hitEnd = False
		if self.activeGroup == len(self.groups) - 1:
			hitEnd = groupToShift.contains(self.length)
		else:
			hitEnd = groupToShift.overlaps(self.groups[self.activeGroup + 1])

		if hitEnd:
			pass



	# End Sequence

class Group:
	'''
	Maintains a start and end index for a group of a particular length. 
	The values start and end are inclusive.'''

	def __init__(self, length = 1, start = 0):
		self.length = max(1, length)
		self.setStart(max(0, start))
		return

	def __iter__(self):
		return iter(range(self.start, self.end + 1))

	def updateEnd(self):
		self.end = self.start + self.length - 1
		return self.end

	def setStart(self, start = 0):
		self.start = start
		self.initial = start
		return self.updateEnd()

	def shift(self, distance = 1):
		self.start += distance
		return self.updateEnd()

	def contains(self, index):
		return self.start <= index and index <= self.end

	def adjacent(self, index):
		return self.start - 1 == index or self.end + 1 == index

	def overlaps(self, otherGroup):
		adjacent = self.adjacent(otherGroup.start) or self.adjacent(otherGroup.end)
		containsOther = self.contains(otherGroup.start) or self.contains(otherGroup.end)
		otherContains = otherGroup.contains(self.start) or otherGroup.contains(self.end)
		return adjacent or containsOther or otherContains

	# End Group

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

	# End PuzzleUtil
	