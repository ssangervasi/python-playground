# def loopTest(breadth, depth):
# 	results = []
# 	arr = [-1 for i in range(breadth)]
# 	active = 0
# 	while active > -1:
# 		if active >= breadth:
# 			active -= 1
# 			continue

# 		arr[active] += 1
# 		if arr[active] == depth:
# 			arr[active] = -1
# 			active -= 1
# 			continue
		
# 		active += 1
# 		results.append(''.join(str(max(val, 0)) for val in arr))

# 	return results
	
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
