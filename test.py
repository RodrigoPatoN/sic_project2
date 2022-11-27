import numpy as np
import pandas as pd

aa = pd.read_csv('sensors_sample_data.csv', header=None)

array = np.array(aa)

print(aa)
print(array[:, 0])