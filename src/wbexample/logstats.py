import numpy as np

# private functions
def _is_odd(num):
    return num & 0x1

def _to_linear(level):
  return 10**(level/10.)

def _to_level(linear):
  return 10*np.log10(linear)

# public functions
def arithmetic_mean(arr):
    
    lin = _to_linear(np.array(arr))
    return _to_level(np.mean(lin))

def arithmetic_median(arr):
    arr = np.array(np.sort(arr))
    length = len(arr)
    if _is_odd(length):
        return np.median(arr)
    else:
        ihalf = int(length/2)
        mean_arr = arr[ihalf-1:ihalf+1]
        return arithmetic_mean(mean_arr)
    
def nan_arithmetic_mean(arr):
    return arithmetic_mean(arr[np.isfinite(arr)])

def nan_arithmetic_median(arr):
    return arithmetic_median(arr[np.isfinite(arr)])