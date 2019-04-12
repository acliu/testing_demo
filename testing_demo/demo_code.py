import numpy as np

def rand_arr(size):
    """
    Returns a random Gaussian array of shape (size, size)
    """
    return np.random.normal(size=(size,size))

def hardcoded_arr():
    """
    Returns a silly hard coded array
    """
    return np.array(((3.2000001, 0.0), (0.0, 8.9)))

def error_msg(x):
    if not isinstance(x, str):
        raise TypeError("Input should be a string")

