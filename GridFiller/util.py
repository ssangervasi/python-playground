def loopTest(breadth, depth):
	results = []
	arr = [0 for i in range(breadth)]
	right = active = first = 0
	# for BIGLOOP in range(depth ** breadth):
	while right < breadth:
		hitBoundary = True
		for index in range(first, active + 1):
			if hitBoundary:
				arr[index] = (arr[index] + 1)
				hitBoundary = arr[index] >= depth
			else:
				break
		
		if hitBoundary:
			active += 1
			arr = [0 if i <= active + 1 else arr[i] for i in range(breadth)]
			if active < breadth:
				arr[active] = 1

		if active > right:
			# print("right", active, right)
			right += 1
			active = first

		results.append(''.join(str(val) for val in arr))

	return results

testRes = loopTest(3, 2)
print(testRes)
print("Actual", len(testRes))
print("Unique", len(set(testRes)))

def recursionTest(breadth, depth):
	results = set()
	recursionHelper(0, depth, [0 for i in range(breadth)], results)
	return results

def recursionHelper(index, depth, arr, results):
	if index >= len(arr):
		return
	for myDepth in range(depth):
		nextArr = arr.copy()
		nextArr[index] = myDepth
		results.add(''.join(str(val) for val in nextArr))
		recursionHelper(index + 1, depth, nextArr, results)

testRes = recursionTest(3, 2)
print(testRes)
print("Actual", len(testRes))
print("Unique", len(set(testRes)))
