import numpy as np
import numpy.typing as npt


# private functions
def _is_odd(num: int) -> int:
    """Returns boolean int (i.e. 1 if num is odd, 0 if num is even)"""
    return num & 0x1


def _to_linear(level: float | npt.ArrayLike) -> float | np.ndarray:
    """converts level(s) to linear quantity(ies)"""
    return 10 ** (level / 10.0)


def _to_level(linear: float | npt.ArrayLike) -> float | np.ndarray:
    """converts linear quantity(ies) to level(s)"""
    return 10 * np.log10(linear)


# public functions
def arithmetic_mean(arr: npt.ArrayLike) -> float:
    """
    Calculate the arithmetic mean from a list of levels

    Parameters
    ----------
    arr : npt.ArrayLike
        List/Array of levels

    Returns
    -------
    float
        arithmetic mean

    """
    lin = _to_linear(np.array(arr))
    return _to_level(np.mean(lin))


def arithmetic_median(arr: npt.ArrayLike) -> float:
    """
    Calculate the arithmetic median from a list of levels

    Parameters
    ----------
    arr : npt.ArrayLike
        List/Array of levels

    Returns
    -------
    float
        arithmetic median

    """
    arr = np.array(np.sort(arr))
    length = len(arr)
    if _is_odd(length):
        return np.median(arr)
    else:
        ihalf = int(length / 2)
        mean_arr = arr[ihalf - 1 : ihalf + 1]
        return arithmetic_mean(mean_arr)


def nan_arithmetic_mean(arr: npt.ArrayLike) -> float:
    """
    Calculate the arithmetic mean from a list of levels which may contain
    nans.

    Parameters
    ----------
    arr : npt.ArrayLike
        List/Array of levels

    Returns
    -------
    float
        arithmetic mean

    """
    return arithmetic_mean(arr[np.isfinite(arr)])


def nan_arithmetic_median(arr: npt.ArrayLike) -> float:
    """
    Calculate the arithmetic mean from a list of levels which may contain
    nans.

    Parameters
    ----------
    arr : npt.ArrayLike
        List/Array of levels

    Returns
    -------
    float
        arithmetic mean

    """
    return arithmetic_median(arr[np.isfinite(arr)])
