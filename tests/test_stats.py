from wbexample import logstats
import numpy as np

test_levels = [151,163,156,161,164,173]

def test_mean():

    mean = logstats.arithmetic_mean(test_levels)
    print(f'mean={mean} dB')
    expected = 166.40857216012822
    assert np.isclose(mean,expected)

def test_median():
    median = logstats.arithmetic_median(test_levels)
    print(f'median={median} dB')
    expected = 162.1141260713036
    assert np.isclose(median,expected)


print(type(logstats._is_odd(5)))