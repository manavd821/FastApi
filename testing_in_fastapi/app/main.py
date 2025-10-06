import asyncio

add : int = lambda a,b : a+b 
def divide(a: int, b: int) -> float:
	if b == 0:
		raise ValueError("cannot divide by zero")
	return a / b

async def async_add(a,b):
	await asyncio.sleep(1)
	return a+b

async def async_divide(a: int, b: int) -> float:
	await asyncio.sleep(1)
	if b == 0:
		raise ValueError("cannot divide by zero")
	return a / b