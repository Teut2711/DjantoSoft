import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\window\\aggregations.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.window.aggregations'
__package__ = 'pandas._libs.window'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def ewma():
    '\n    Compute exponentially-weighted moving average using center-of-mass.\n\n    Parameters\n    ----------\n    vals : ndarray (float64 type)\n    com : float64\n    adjust: int\n    ignore_na: bool\n    minp: int\n\n    Returns\n    -------\n    ndarray\n    '
    pass

def ewmcov():
    '\n    Compute exponentially-weighted moving variance using center-of-mass.\n\n    Parameters\n    ----------\n    input_x : ndarray (float64 type)\n    input_y : ndarray (float64 type)\n    com : float64\n    adjust: int\n    ignore_na: bool\n    minp: int\n    bias: int\n\n    Returns\n    -------\n    ndarray\n    '
    pass

interpolation_types = _mod_builtins.dict()
def is_monotonic(arr, timelike):
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    pass

def roll_count():
    pass

def roll_generic_fixed():
    pass

def roll_generic_variable():
    pass

def roll_kurt_fixed():
    pass

def roll_kurt_variable():
    pass

def roll_max_fixed():
    "\n    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    closed : 'right', 'left', 'both', 'neither'\n            make the interval closed on the right, left,\n            both or neither endpoints\n    "
    pass

def roll_max_variable():
    "\n    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    closed : 'right', 'left', 'both', 'neither'\n            make the interval closed on the right, left,\n            both or neither endpoints\n    "
    pass

def roll_mean_fixed():
    pass

def roll_mean_variable():
    pass

def roll_median_c():
    pass

def roll_min_fixed():
    '\n    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    '
    pass

def roll_min_variable():
    '\n    Moving min of 1d array of any numeric type along axis=0 ignoring NaNs.\n\n    Parameters\n    ----------\n    values : np.ndarray[np.float64]\n    window : int, size of rolling window\n    minp : if number of observations in window\n          is below this, output a NaN\n    index : ndarray, optional\n       index for window computation\n    '
    pass

def roll_quantile():
    '\n    O(N log(window)) implementation using skip list\n    '
    pass

def roll_skew_fixed():
    pass

def roll_skew_variable():
    pass

def roll_sum_fixed():
    pass

def roll_sum_variable():
    pass

def roll_var_fixed():
    "\n    Numerically stable implementation using Welford's method.\n    "
    pass

def roll_var_variable():
    "\n    Numerically stable implementation using Welford's method.\n    "
    pass

def roll_weighted_mean():
    pass

def roll_weighted_sum():
    pass

def roll_weighted_var():
    "\n    Calculates weighted rolling variance using West's online algorithm.\n\n    Paper: https://dl.acm.org/citation.cfm?id=359153\n\n    Parameters\n    ----------\n    values: float64_t[:]\n        values to roll window over\n    weights: float64_t[:]\n        array of weights whose length is window size\n    minp: int64_t\n        minimum number of observations to calculate\n        variance of a window\n    ddof: unsigned int\n         the divisor used in variance calculations\n         is the window size - ddof\n\n    Returns\n    -------\n    output: float64_t[:]\n        weighted variances of windows\n    "
    pass

