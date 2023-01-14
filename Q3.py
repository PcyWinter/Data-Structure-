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

	def addTail(self,key):
		node = Node(key,None)
		if self.list != None:
			cur = self.list
			while cur.next != None:
				cur = cur.next
			cur.next = node
		else:
			self.list = node
		self.size += 1

	def adjustTail(self):
		if self.size <= 0:
			return;

		tailIndex = self.size-1
		tailNode = self.getNode(tailIndex)
		parent = self.getParent(tailIndex)

		tailValue = tailNode.key
		while tailIndex > 0 and tailValue < parent.key:
			tailNode.key = parent.key

			tailIndex = (tailIndex-1)//2
			tailNode = parent
			parent = self.getParent(tailIndex)
		tailNode.key = tailValue

	def deleteHead(self):
		if self.size > 1:
			lastTwo = self.getNode(self.size-2) # 获取队列尾结点的前一个
			self.list.key =  lastTwo.next.key # 队列尾值放到队列头
			lastTwo.next = None # 删掉最后一个节点
		else:
			self.list = None
		self.size -= 1 # 长度减一

	def adjustHead(self):
		if self.size <= 0:
			return;

		headIndex = 0
		headNode = self.getNode(headIndex)
		headValue = headNode.key
		while 2*headIndex+1 < self.size:
			node = self.getLeftChild(headIndex)
			right = self.getRightChild(headIndex)

			headIndex = headIndex*2 + 1
			if right != None and right.key < node.key :
				node = right
				headIndex = headIndex*2 + 2

			if headValue > node.key:
				headNode.key = node.key
				headNode = node
			else:
				break
		headNode.key = headValue

	''' 
	第3小题时间复杂度分析：
	addTail(key)函数需要遍历整个链表，故时间复杂度为O(n),
	adjustTail()函数获取父节点时间复杂度为O(n),调整耗费时间复杂度为o(logn),故时间复杂度为O(nlogn)
	故插入元素insert()函数的时间复杂度为O(nlogn)
	'''
	def insert(self,key):
		self.addTail(key)
		self.adjustTail() # 最后一个元素上浮

	''' 
	第3小题时间复杂度分析：
	deleteHead()函数获取倒数第二个节点时需要遍历整个链表，故时间复杂度为O(n),
	adjustHead()函数获取左右孩子节点时间复杂度为O(n),调整耗费时间复杂度为o(logn),故时间复杂度为O(nlogn)
	故删除元素delMin()函数的时间复杂度为O(nlogn)
	'''
	def delMin(self):
		if self.size <= 0:
			return;
			
		self.deleteHead()
		self.adjustHead() # 第一个元素下沉

