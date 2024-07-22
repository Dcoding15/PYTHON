'''

AsyncIO - It is programmign pattern that allowds for high performance I/O operations in a concurrent and non-blocking manner.

'''

import asyncio

async def fun1():
	await asyncio.sleep(1)
	print("This is async operations 1")

async def fun2():
	await asyncio.sleep(5)
	print("This is async operations 2")

async def fun3():
	await asyncio.sleep(3)
	print("This is async operations 3")

async def main():
    # Creating single task
    # await asyncio.create_task(fun1())
    # await asyncio.create_task(fun2())
    # await asyncio.create_task(fun3())
    
    # Creating multiple task executing in parallel
    await asyncio.gather(fun1(),fun2(),fun3())

asyncio.run(main())