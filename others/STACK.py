stack_limit = 10	# stack size limit
stack = []

def push():
    if stack_limit == len(stack):
        print("STACK Overflow\n")
    else:
        stack.append(input("PUSH ELEMENT: "))

def pop():
    if len(stack) == 0:
        print("STACK Underflow\n")
    else:
        print("POP ELEMENT:",stack.pop())

def display():
	print("STACK:",stack)

if __name__ == '__main__':
    while(True):
        print("\t Operation for STACK: -")
        print("\t 	1. PUSH")
        print("\t 	2. POP")
        print("\t 	3. DISPLAY")
        print("\t 	4. EXIT")
        option = int(input("Enter your option: "))
        if option == 1:
            push()
        elif option == 2:
            pop()
        elif option == 3:
            display()
        elif option == 4:
            break
