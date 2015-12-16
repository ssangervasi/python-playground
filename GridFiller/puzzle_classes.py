
class Sequence:
	'''Wraps a sequence of 0's and 1's and maintains the state of possible sequences.'''

	def __init__(self, pattern, state):
		self.length = len(state)
		self.pattern = [int(groupLen) for groupLen in pattern]
		self.initialState = [int(bit) for bit in state]
		self.prefilled = [index for index in range(self.length) if self.initialState[index] > 0 ]
		self.groups = [Group(nextLen) for nextLen in pattern]
		self.invalidStates = set()
		self.setInitialState()
		return

	def spreadGroups(self):
		nextStart = 0
		lastGroup = None
		for group in self.groups:
			group.setStart(nextStart)
			nextStart = group.end + 2
			lastGroup = group

		return (not lastGroup) or lastGroup.end < self.length

	def setInitialState(self):
		self.stateIndex = 0
		self.spreadGroups()
		self.state = PuzzleUtil.stateForGroups(self.groups, self.length)
		self.last = len(self.groups) - 1
		self.active = self.last
		self.left = self.last
		self.edgeLeft = Group(start = -2)
		self.edgeRight = Group(start = self.length + 1)
		self.printState(header = True)
		return self.state

	def nextState(self):
		if not self.state:
			return self.setInitialState()

		self.stateIndex += 1
		self.shiftGroups()

		if self.left < 0:
			self.setInitialState()
			self.stateIndex = 0	
		# while self.stateIndex in self.invalidStates:
		# 	self.stateIndex += 1
		# 	self.shiftGroups()

		# Default sequence has some bits filled
		newState = self.initialState.copy()
		PuzzleUtil.stateForGroups(self.groups, state = newState)
		if PuzzleUtil.matches(self.pattern, newState):
			self.state = newState
			self.printState("Valid State")
		else:
			self.printState("Invalid state", newState)
			self.invalidStates.add(self.stateIndex)
			# self.nextState()

		return self.state

	def shiftGroups(self):
		groupIndex = self.active
		hitBoundary = True
		activeHit = False
		while hitBoundary:
			hitBoundary = self.cycleGroup(groupIndex)
			if groupIndex < self.last:
				groupIndex += 1
			else:
				hitBoundary = False

		if groupIndex > self.last:
			# print("GI", groupIndex, self.active)
			self.active -= 1

		if self.active < self.left:
			# print("LEFT", self.active, self.left)
			self.left -= 1
			self.active = self.last
			return True

		return False

	def cycleGroup(self, groupIndex):
		group = self.groups[groupIndex]
		groupOnRight = self.groups[groupIndex + 1] if groupIndex < self.last else self.edgeRight
		group.shift()
		if group.overlaps(groupOnRight):
			print("X overlaps Y", group, self.edgeRight)
			groupOnLeft = self.groups[groupIndex - 1] if groupIndex >= 0 else self.edgeLeft
			newStart = groupOnLeft.end + 2
			group.setStart(newStart)
			return True

		return False

	# End Sequence

	def printState(self, message = '', state = None, header = False):
		state = state or self.state
		if (header):
			print("State:\t{0}\t{1}\t{2}\t{3}".format('Index', 'Active', 'Left', 'State'))
		print("State:\t{0:3d}\t{1:3d}\t{2:3d}\t{3}\t|\t{4}".format(self.stateIndex, self.active, self.left, state, message))

class Group:
	'''
	Maintains a start and end index for a group of a particular length. 
	The values start and end are inclusive.'''

	def __init__(self, length = 1, start = 0):
		self.length = max(1, length)
		self.setStart(start)
		return

	def __iter__(self):
		return iter(range(self.start, self.end + 1))

	def __str__(self):
		return '({0}, {1})'.format(self.start, self.end)

	def updateEnd(self):
		self.end = self.start + self.length - 1
		return self.end

	def setStart(self, start = 0):
		self.start = start
		self.initial = start
		return self.updateEnd()

	def shiftStart(self, distance = 1):
		return self.setStart(self.initial + distance)

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
	