#! /usr/bin/python3
# Tower of Hanoi Problem

def towerofhanoi(disc:int, rod1:int, rod2:int, rod3:int) -> None:
	if disc == 1:
		print(f'Move disc {disc} from rod {rod1} to end {rod3}')
		return
	towerofhanoi(disc-1, rod1, rod3, rod2)
	print(f'Move disc {disc} from rod {rod1} to rod {rod3}')
	towerofhanoi(disc-1, rod2, rod1, rod3)

towerofhanoi(3,"A","B","C")
