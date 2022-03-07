import numpy as np
import asyncio
import os
import time


async def __multiply__():
    """Creates two numpy arrays of size 10000 x 10000 and multiplies and return the result

    Returns:
        np.array: Multiplication result of two numpy arrays
    """
    a1 = np.random.rand(10000, 10000)
    a2 = np.random.rand(10000, 10000)
    mul = np.multiply(a1, a2)
    return mul


async def array_multiply(num):
    """Runs the __multiply__ function `num` number time

    Args:
        num (int): number of time the function is getting executed. Just to print

    Returns:
        List[List]: flattened list of randomly multplied arrays
    """
    print(f'MULTIPLYING FOR NUM: {num}')
    mul = await __multiply__()
    print(f'MULTIPLIED FOR NUM {num}')
    print(f'SHAPE: {mul.shape}')
    return mul.flatten().tolist()


async def multiple_array_multiply(n=2):
    """Runs the `array_multiply` in an async manner n number of times

    Args:
        n (int, optional): Number of times to run the `array_multiply` function. Defaults to 2.

    Returns:
        List[List]: Flattened list of randomly multiplied arrays
    """
    results = await asyncio.gather(*[array_multiply(_) for _ in range(n)],
                                   return_exceptions=True)
    return results


def multiply_util(n=2):
    """Runs the `multiple_array_multiply` function inside an 
    event loop to run `array_multiply` function asynchronously

    Args:
        n (int, optional): Number of times to run `array_multiply` function. Defaults to 2.

    Returns:
        List[List]: Flattened list of randomly multiplied arrays for `n` executions
    """
    loop = asyncio.new_event_loop()
    try:
        result = loop.run_until_complete(multiple_array_multiply(n=n))
    finally:
        loop.close()

    return result