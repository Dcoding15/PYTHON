#! /usr/bin/python3

# Single Linked List

class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def insertAtBegin(self, data):
		nlist = node(data)
		if self.head is None:
			print(f"Element {nlist.data} inserted")
			self.head = nlist
			return self
		else:
			print(f"Element {nlist.data} inserted")
			nlist.next = self.head
			self.head = nlist
			return self

	def insertAtPosition(self, data, position):
	    nlist = node(data)
		size = self.countlist()
	    if position > size:
	    	self.insertAtEnd(data)
	    elif position <= 1:
	    	self.insertAtBegin(data)
	    else:
	    	clist = self.head
	    	count = 1
	    	while count != position-1:
	    		count += 1
       			clist = clist.next
	    	print(f"Element {nlist.data} inserted")
	    	nlist.next = clist.next
	    	clist.next = nlist
	    	return self

	def insertAtEnd(self, data):
		nlist = node(data)
		if self.head is None:
			print(f"Element {nlist.data} inserted")
			self.head = nlist
			return self
		else:
			olist = self.head
			while olist.next is not None:
				olist = olist.next
			print(f"Element {nlist.data} inserted")
			olist.next = nlist
			return self

	def update(self, search_value, update_value):
		olist = self.head
		flag = True
		while search_value != olist.data:
			olist = olist.next
			if olist.next == None:
				flag = False
				break
		if flag == False:
			print(f"Element {search_value} Not Found")
		else:
			print(f"Element updated from {search_value} to {update_value}")
			olist.data = update_value

	def removeAtBegin(self):
		olist = self.head
		if olist is None:
			print("Empty linked list")
		else:
			print(f"Element {self.head.data} removed")
			self.head = olist.next
			return self

	def removeAtPosition(self, position):
		size = self.countlist()
		if position >= size:
			self.removeAtEnd()
		elif position <= 1:
			self.removeAtBegin()
		else:
			clist = self.head
			count = 1
			while count != position-1:
				count += 1
				clist = clist.next
			if clist.next.next is None:
				print(f"Element {clist.next.data} removed")
				clist.next = None
				return self
			else:
				print(f"Element {clist.next.data} removed")
				clist.next = clist.next.next
				return self

	def removeAtEnd(self):
		olist = self.head
		if olist is None:
			print("Empty linked list")
		elif olist.next is None:
			print(f"Element {olist.data} removed")
			self.head = None
		else:
			while(olist.next.next is not None):
				olist = olist.next
			print(f"Element {olist.next.data} removed")
			olist.next = None
			return self

	def countlist(self):
	    olist = self.head
	    count = 0
	    while olist is not None:
	        olist = olist.next
	        count += 1
	    return count

	def traverse(self):
		olist = self.head
		while olist is not None:
			print(olist.data)
			olist = olist.next

# Creation of single linked list
llist = linkedlist()

# Inserting new node at begin of single linked list
#llist.insertAtBegin(10)
#llist.insertAtBegin(20)
#llist.insertAtBegin(30)
#llist.insertAtBegin(40)

# Inserting new node at position of single linked list
#llist.insertAtPosition('a',-1)
#llist.insertAtPosition('a',1)
#llist.insertAtPosition('a',2)
#llist.insertAtPosition('a',3)
#llist.insertAtPosition('a',4)
#llist.insertAtPosition('a',5)

# Inserting new node at end of single linked list
#llist.insertAtEnd(10)
#llist.insertAtEnd(20)
#llist.insertAtEnd(30)
#llist.insertAtEnd(40)

# Removing existing node from begin of single linked list
#llist.removeAtBegin()
#llist.removeAtBegin()
#llist.removeAtBegin()
#llist.removeAtBegin()
#llist.removeAtBegin()

# Removing existing node from any position of single linked list
#llist.removeAtPosition(-1)
#llist.removeAtPosition(1)
#llist.removeAtPosition(2)
#llist.removeAtPosition(3)
#llist.removeAtPosition(4)
#llist.removeAtPosition(5)

# Removing existing node from end of single linked list
#llist.removeAtEnd()
#llist.removeAtEnd()
#llist.removeAtEnd()
#llist.removeAtEnd()
#llist.removeAtEnd()

# Updating existing node data with new data
#llist.update(10,'abc')
#llist.update(20,'abc')
#llist.update(30,'abc')
#llist.update(40,'abc')
#llist.update(500,'abc')

# Traversing single linked list
#llist.traverse()

#Time Complexity: -
# Insertion at beginnig     : O(1)
# Insertion at any position : O(n)
# Insetion at ending        : O(n)
# Deletion at beginnig      : O(1)
# Deletion at any position  : O(n)
# Deletion at ending        : O(n)
# Traverse                  : O(n)

#Space Complexity: O(1) (because of creating one temporary variable)
