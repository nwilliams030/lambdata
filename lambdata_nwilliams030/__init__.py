""" lambdata - a collection of data science helper functions """

import pandas as pd
import numpy as np

#Sample code
ONES = pd.DataFrame(np.ones(10))
ZEROES = pd.DataFrame(np.zeros(50))

#Sample functions
def increment(x):
    return (x + 1)
