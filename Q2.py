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
	第2小题解释：最小优先级队列插入元素时包括将元素添加至链表尾部和将链表尾部元素上浮两个操作，使用addTail(key)
	函数时创建包含值key的节点，并将新生成节点通过尾插法插入到链表尾部，使用adjustTail()函数时，用于将
	新插入的节点调整到最小优先级队列的合适位置，即堆的合适位置，实现过程主要通过类似递归操作实现当前节点
	与父节点	比较，若父节点值更大，则当前节点值上浮，若父节点值更小，则结束调整
	'''
	def insert(self,key):
		self.addTail(key)
		self.adjustTail() # 最后一个元素上浮

	''' 
	第2小题解释：最小优先级队列删除元素时包括将链表尾部元素覆盖头部元素和链头元素下沉两个操作，
	使用deleteHead()	函数时，将链表最后一个节点值覆盖链表头部节点值，再删除链表最后一个节点，
	使用adjustHead()函数时，将堆顶节点调整到最小优先级队列的合适位置，即堆的合适位置，
	实现过程主要通过类似递归操作实现当前节点与左右孩子节点比较，
	若左右孩子节点值更小，则当前节点值下沉，若父节点值更大，则结束调整
	'''
	def delMin(self):
		if self.size <= 0:
			return;

		self.deleteHead()
		self.adjustHead() # 第一个元素下沉