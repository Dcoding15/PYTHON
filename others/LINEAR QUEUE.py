linear_queue_limit = 10	# linear linear_queue size limit
linear_queue = []

def insert():
    if len(linear_queue) == linear_queue_limit:
        print("LINEAR linear_queue Overflow")
    else:
        linear_queue.append(input("INSERT ELEMENT: "))

def delete():
    if len(linear_queue) == 0:
        print("LINEAR linear_queue Underflow")
    else:
        print("DELETE ELEMENT:",linear_queue.pop(0))

def display():
    print("LINEAR linear_queue:",linear_queue)

if __name__ == '__main__':
    while(True):
        print("\t Operation for LINEAR linear_queue: -")
        print("\t 	1. INSERT")
        print("\t 	2. DELETE")
        print("\t 	3. DISPLAY")
        print("\t 	4. EXIT")
        option = int(input("Enter your option: "))
        if option == 1:
            insert()
        elif option == 2:
            delete()
        elif option == 3:
            display()
        elif option == 4:
            break