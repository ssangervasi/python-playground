'''
Python 2.7
Thread: https://www.reddit.com/r/computerscience/comments/4yvbos/faster_sorting_algorithm/
'''
__author__ = 'flipkitty'

import random
import itertools
from collections import defaultdict 

class PermuteSorter(object):
	# Shared between classes.
	permutations = defaultdict(list)
	cached = defaultdict(bool)
	UP = '1'
	DOWN = '0'

	def sort(self, to_sort):
		length = len(to_sort)
		# Construct data.
		self.permute(length)
		updowns = self.updown_hash(to_sort)
		perm_indicies = defaultdict(int)
		# Apply transforms until list is monotonic.
		while self.DOWN in updowns:
			# This is where all of the time complexity is.
			# How do we choose the right tranform to use?
			trans_list = self.permutations[updowns]
			trans_index = perm_indicies[updowns]
			trans = trans_list[trans_index]
			perm_indicies[updowns] = (trans_index + 1) % len(trans_list)
			# Apply transform and rehash
			to_sort = self.transform(to_sort, trans)
			updowns = self.updown_hash(to_sort)
		return to_sort

	def permute(self, n):
		# Prevent memory 'splode.
		if len(self.permutations) > 1000:
			self.permutations = defaultdict(list)
			self.cached = defaultdict(bool)
		if self.cached[n]:
			return
		base_list = range(n)
		# O(n^2) time.
		for perm in itertools.permutations(base_list):
			updowns = self.updown_hash(perm)
			self.permutations[updowns].append(perm)
		self.cached[n] = True

	def updown_hash(self, perm):
		hash_list = []
		for i in xrange(len(perm) - 1):
			left, right = perm[i:i+2]
			if left <= right:
				hash_list.append(self.UP)
			else:
				hash_list.append(self.DOWN)
		return ''.join(hash_list)

	def transform(self, to_trans, trans):
		return [to_trans[i] for i in trans]


def test_permute_sorter(fail_fast=False):
	ps = PermuteSorter()
	for length in xrange(0, 15, 3):
		shuffled = [random.randint(-100, 100)
								for digit in xrange(length)]
		ps_sorted = ps.sort(shuffled)
		py_sorted = sorted(shuffled)
		if ps_sorted != py_sorted:
			print '\nExpected: {}\nFound: {}\n'.format(py_sorted, ps_sorted)
			if fail_fast:
				break
		else:
			print 'Yay: ', ps_sorted

test_permute_sorter(True)