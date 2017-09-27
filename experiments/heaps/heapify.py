# impliment heapsort with the heap both in a tree structure and an array.
# time the resulting algos against each other
import numpy as np
import math

def height(nodes):
	return int(math.log2(nodes + 1) - 1)

def nodes(height):
	return int(2**(height + 1) - 1)

class ArrayHeap(object):
	'''
	Array implementation of a heap
	'''

	def __init__(self, data):
		self.dataLen = len(data)
		self.heap = data
		self.m = 0

	def left(self, i):
		return 2*i
	
	def right(self, i):
		return 2*i + 1

	def parent(self, i):
		return int(i/2)

	def isLeaf(self, i):
		return self.left(i) > self.count
	
	def isRoot(self, i):
		return i == 1
	
	def shiftDown(self, pos, lim):
		'''
		Ensure that every parent is smaller that its childern
		or ensure that every child is smaller than its parent
		'''
		left = self.left(pos)
		right = self.right(pos)
		
		if right < lim:
			if self.heap[right] < self.heap[pos]: # swap, but first check that the left isnt smaller
				if self.heap[left] < self.heap[right]:
					self.swap(left, pos)
					self.shiftDown(left, lim)
				else:
					self.swap(right, pos)
					self.shiftDown(right, lim)
		
		elif left < lim: # this is the last element in the list
			if self.heap[left] < self.heap[pos]: # swap
				self.swap(left, pos)
				return
		else: # reached end of list
			return
	
	def makeHeap(self):
		'''
		Start with the data loaded into the array,
		step through the heap starting from the leaf nodes
		Check against there parents and switch is necessary,
		'''
		self.m = self.dataLen
		for count in range(1, int(self.dataLen)):
			pos = self.dataLen - count - 1
			self.heapify(pos)

	def heapify(self, pos):
		left = self.left(pos)
		right = self.right(pos)
		minVal = pos
		if(left < self.m and self.heap[left] < self.heap[minVal]):
			minVal = left
		if(right < self.m and self.heap[right] < self.heap[minVal]):
			minVal = right

		if minVal != pos: # swap
			self.swap(pos, minVal)
			self.heapify(minVal)
		
	def swap(self, posA, posB):
		temp = self.heap[posA]
		self.heap[posA] = self.heap[posB]
		self.heap[posB] = temp

	def extract(self):
		valOut = self.heap[0]
		self.heap[0] = self.heap[self.m - 1]
		self.heap[self.m - 1] = ''
		self.m -= 1
		self.heapify(0)
		return valOut
	
	def heapSort(self):
		sortArray = [None]*(self.dataLen)
		while self.m > 0:
			sortArray[self.m] = self.extract()
		return (sortArray)

class TreeHeap(object):
	'''
	Binary tree implimentation of a heap
	'''
	def __init__(self, data):
		self.data = data
		self.root = Node(parent = None, value = self.data.pop())
		self.height = 0
		self.nodes = 0
		self.nodeArray = [self.root]

	def heapify(self, node):
		#if node.isLeaf:
		#	return
		smallNode = node
		if node.left is not None and node.left.value < smallNode.value: # swap them
			smallNode = node.left

		if node.right is not None and node.right.value < smallNode.value:
			smallNode = node.right

		if smallNode is not node:
			self.swap(top = node, bottom = smallNode)
			self.heapify(smallNode)

	def swap(self, top, bottom):
		'''
		Swap 2 nodes that can be either parent child or siblings or random entries
		'''
		tl = top.left
		tr = top.right
		tp = top.parent
		tPos = top.isLeft
		
		bl = bottom.left
		br = bottom.right
		bp = bottom.parent
		bPos = bottom.isLeft

		bottom.left = tl
		bottom.right = tr

		top.left = bl
		top.right = br

		if bottom is tl: # bottom is the left node of top
			top.parent = bottom
			bottom.left = top
		
		elif bottom is tr: # bottom is the right node of top
			top.parent = bottom
			bottom.right = top

		elif bottom is tp:
			self.swap(top = bottom, bottom=top)
			# raise Exception("Bottom cannot be the parent of top")

		else:
			# top and bottom are siblings
			bottom.parent = tp
			top.parent = bp
			if bPos: # bottom is left node
				bp.left = top
			else: # bottom is right node
				bp.right = top
			
			if tp is None:
				return
			elif tPos: # top is left node
				tp.left = bottom
			else: # top is right node
				tp.right = bottom

	@property
	def	leftestNode(self):
		node = self.root
		while node.isFull:
			node = node.left
		return node

	@property
	def newLayer(self):
		nodes(self.height) == self.nodes # full layer
	
	@property
	def nextInsertion(self):
		if self.newLayer:
			self.height += 1
			root = self.leftestNode
		else:
			root = self.searchParentRight(root = self.leftestNode)
		return root

	def searchParentRight(self, root):
		'''
		Climb the tree, checking the parents right
		if the current node is the right node climb
		until at root or in a left branch.
		When you get to a left branch climb down to the left
		until you find the leftest node with an empty left, 
		return the root
		'''

		# climbing
		while root.isFull:
			if root.parent.isFull:
				root = root.parent # climb
				continue
			else:
				root = root.parent.right # fond the connecting branch
				break
		
		# descending
		while True:
			if not root.isFull:
				break
			else:
				root = root.left
		return root

	def addNode(self, data):
		root = self.nextInsertion
		node = Node(parent=root, value=data)
		
		if root.left is None:
			root.left = node
		elif root.right is None:
			root.right = node
		else:
			raise Exception("Impossible case")
		self.nodeArray.append(node)
		self.nodes += 1

	def makeHeap(self):
		try:
			while True:
				self.addNode(self.data.pop())
		except IndexError:
			pass
		
		for node in self.nodeArray:
			self.heapify(node)

	def heapSort(self):
		sortedArray = [0]*self.nodes
		while self.nodes >= 0:
			sortedArray[self.nodes - 1] = self.root.value
			lastNode = self.nodeArray.pop()
			self.swap(top=self.root, bottom=lastNode)
			self.root.unlink()
			self.root = lastNode
			self.heapify(self.root)
			self.nodes -= 1
		print(sortedArray)

class Node(object):
	'''
	Binary tree heap node
	'''

	def __init__(self, parent, value):
		self.parent = parent
		self.left = None
		self.right = None
		self.value = value
	
	def unlink(self):
		self.left = None
		self.right = None

	@property
	def isRoot(self):
		return self.parent is None
	
	@property
	def isLeaf(self):
		return self.left is None and self.right is None
	
	@property
	def isFull(self):
		return self.left is not None and self.right is not None
	
	@property
	def isRight(self):
		if self.isRoot:
			return False
		return self.parent.right is self

	@property
	def isLeft(self):
		if self.isRoot:
			return False
		return self.parent.left is self

def makeRandomData(dataLen, seed):
	'''
	Define a data length (i.e. n) of data positions to run,
	seed a random number generator to make a generator for 
	random numbers.
	'''
	import random
	rand = random.SystemRandom()
	rand.seed(seed)
	for i in range(dataLen):
		yield rand.getrandbits(5)

def heapSortRace(dataLen, seed):
	'''
	time the sorting of the same data with an array heap, 
	a tree heap, and then with an internal function.
	'''
	import time, copy
	aHeapData = list(makeRandomData(dataLen, seed))
	heapqData = copy.deepcopy(aHeapData)
	tHeapData = copy.deepcopy(aHeapData)
	

	aHeap = ArrayHeap(aHeapData)
	tStart = time.time()
	aHeap.makeHeap()
	tEnd = time.time() - tStart
	print("Array Heap: ", tEnd)

	import heapq
	tStart = time.time()
	heapq.heapify(heapqData)
	tEnd = time.time() - tStart
	print("Heapq: ", tEnd)

	tHeap = TreeHeap(tHeapData)
	tStart = time.time()
	tHeap.makeHeap()
	tEnd = time.time() - tStart
	print("THeap: ", tEnd)

	resp = aHeap.heapSort()
	
	rCopy = copy.deepcopy(resp)
	rCopy.reverse()
	
	resp.sort()
	assert(rCopy == resp)
	#heapq.sort()
	tHeap.heapSort()

if __name__ == "__main__":
	heapSortRace(50, 2)
