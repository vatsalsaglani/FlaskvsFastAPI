import numpy as np


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
