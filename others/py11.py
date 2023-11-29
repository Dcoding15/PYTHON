#! /usr/bin/python3

def f1():
	from pack.pack1.fibo import fibo
	fibo()

def f2():
	from pack.pack2.factorial import facto
	facto()

def fun():
	print("\n1.Fibonacci Sequence\n2.Factorial\n")
	n = eval(input('INPUT: '))
	if n == 1:
		f1()
	elif n == 2:
		f2()
	else:
		fun()

fun()
