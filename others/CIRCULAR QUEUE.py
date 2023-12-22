class Circular_Queue:
    circular_queue = []
    high, low = -1, -1
    def __init__(self):
        self.circular_queue_limit = 5	# circular queue size limit
    
    def enqueue(self):
        if len(Circular_Queue.circular_queue) == self.circular_queue_limit:
            print("CIRCULAR QUEUE Overflow\n")
        elif Circular_Queue.high == -1 and Circular_Queue.low == -1:
            Circular_Queue.high, Circular_Queue.low = 0, 0
            Circular_Queue.circular_queue.append(input("ENQUEUE ELEMENT: "))
            print('case 1')
        else:
            Circular_Queue.high = (Circular_Queue.high + 1) % self.circular_queue_limit
            Circular_Queue.circular_queue.append(input("ENQUEUE ELEMENT: "))
            print('case 2')
    
    def dequeue(self):
        if len(Circular_Queue.circular_queue) == 0:
            print("CIRCULAR QUEUE Underflow\n")
        elif Circular_Queue.high == Circular_Queue.low:
            print("POP ELEMENT:",Circular_Queue.circular_queue.pop(Circular_Queue.low))
            Circular_Queue.high, Circular_Queue.low = -1, -1
            print('case 3')
        else:
            print("DEQUEUE ELEMENT:",Circular_Queue.circular_queue.pop(0))
            #Circular_Queue.low = (Circular_Queue.low + 1) % self.circular_queue_limit
            print('case 4')
    
    def display(self):
        print("CIRCULAR QUEUE: ",Circular_Queue.circular_queue)

if __name__ == '__main__':
    while(True):
        print("\t Operation for CIRCULAR QUEUE: -")
        print("\t 	1. ENQUEUE")
        print("\t 	2. DEQUEUE")
        print("\t 	3. DISPLAY")
        print("\t 	4. EXIT")
        cq = Circular_Queue()
        option = int(input("Enter your option: "))
        if option == 1:
            cq.enqueue()
        elif option == 2:
            cq.dequeue()
        elif option == 3:
            print(cq.display())
        elif option == 4:
            break
