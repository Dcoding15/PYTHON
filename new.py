#! /usr/bin/python3

'''
# Tower of Hanoi Problem

def towerofhanoi(disc:int, rod1:int, rod2:int, rod3:int) -> None:
	if disc == 1:
		print(f'Move disc {disc} from rod {rod1} to end {rod3}')
		return
	towerofhanoi(disc-1, rod1, rod3, rod2)
	print(f'Move disc {disc} from rod {rod1} to rod {rod3}')
	towerofhanoi(disc-1, rod2, rod1, rod3)

towerofhanoi(3,"A","B","C")
'''

'''
# Water Jug Problem

def waterjug(cup1:int, cup2:int, target:int) -> None:
	jug1, jug2 = 0, 0
	while jug1 != target or jug2 != 0:
		if jug2 == cup2:
			jug2 = 0
		elif jug1 == 0:
			jug1 = cup1
		else:
			pour = min(jug1, cup2-jug2)
			jug1 -= pour
			jug2 += pour
		print(f'({jug1},{jug2})')
	print(f'Solution: ({jug1},{jug2})')

waterjug(4,3,2)
'''

'''
# BFS - Breadth First Search

from collections import deque

def bfs(graph=dict(), start=None) -> None:
	visited = set()
	queue = deque(start)
	while queue:
		i = queue.popleft()
		if i not in visited:
			print(i, end=' ')
			visited.add(i)
			if graph[i] != {}:
				queue.extend(graph[i] - visited)
			else:
				queue.extend(i)
'''

'''
# DFS - Depth First Search

visited = set()

def dfs(graph=dict(), start=None, visited=None) -> None:
	if visited is None:
		visited = set()
	visited.add(start)
	print(start, end=' ')
	if graph[start] != {}:
		for i in graph[start] - visited:
			dfs(graph, i, visited)
'''

graph = {
	'A' : {'B','C'},
	'B' : {'D','E'},
	'C' : {'B','F'},
	'D' : {},
	'E' : {'F'},
	'F' : {},
}
