class Node:
	def __init__(self, key=None,next=None):
		self.key = key
		self.next = next

class PriorityQueues:
	def __init__(self):
		self.list = None
		self.size = 0

	def getNode(self,index):
		if index < 0 or index > self.size-1:
			return None
		cur = self.list
		for i in range(0,index):
			cur = cur.next
		return cur

	def getParent(self,index):
		parIndex = (index-1)//2
		if parIndex < 0 or parIndex > self.size-1:
			return None
		cur = self.list
		for i in range(0,parIndex):
			cur = cur.next
		return cur

	def getLeftChild(self,index):
		childIndex = 2*index+1
		if childIndex < 0 or childIndex > self.size-1:
			return None
		cur = self.list
		for i in range(0,childIndex):
			cur = cur.next
		return cur

	def getRightChild(self,index):
		childIndex = 2*index+2
		if childIndex < 0 or childIndex > self.size-1:
			return None
		cur = self.list
		for i in range(0,childIndex):
			cur = cur.next
		return cur