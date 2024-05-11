# Doubly Linked List

class node:
	def __init__(self,data):
		self.nxt = None
		self.prv = None
		self.data = data

class doublylinkedlist:
	def __init__(self):
		self.head = None

	def insertAtBegin(self, data):
		nlist = node(data)
		tmp = self.head
		if tmp is None:
			tmp = nlist
			nlist.prv = tmp
			return self
		else:
			nlist.nxt = tmp.nxt
			tmp.prv = nlist
			self.head = nlist
			nlist.prv = self.head
