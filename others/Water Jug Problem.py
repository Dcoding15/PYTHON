#! /usr/bin/python3
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
