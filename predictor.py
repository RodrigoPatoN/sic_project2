import numpy as np

def predict(values):

    mean = np.mean(values)

    if values[0] < mean:

        return 0.9 * mean
    
    else:

        return 1.1 * mean