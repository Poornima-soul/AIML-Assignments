import time
import numpy as np


size = 1_000_000

# Python List
python_list = list(range(size))

start = time.time()
result_list = [x * 2 for x in python_list]
end = time.time()

print("Python List Time:", end - start)

# NumPy Array
numpy_array = np.arange(size)

start = time.time()
result_array = numpy_array * 2
end = time.time()

print("NumPy Array Time:", end - start)


