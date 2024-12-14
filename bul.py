import asyncio

async def hello() -> None:
    await asyncio.sleep(2)
    print("hello")
    


async def bye() -> None:
    print("bye")
    
    
async def main():
    task_1 = asyncio.create_task(hello())
    task_2 = asyncio.create_task(bye())
    
    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())