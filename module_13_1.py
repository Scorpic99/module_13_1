import asyncio
import time


async def start_strongman(name, power):
    spheres = 5
    print(f'Силач {name} начал соревнования.')
    for sphere in range(spheres):
        await asyncio.sleep(1000 / power)
        print(f'Силач {name} поднял {sphere + 1} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Lev', 200))
    task2 = asyncio.create_task(start_strongman('Mark', 1000))
    task3 = asyncio.create_task(start_strongman('Alexio', 500))
    await task1
    await task2
    await task3

start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f"Program time: {finish - start}")
