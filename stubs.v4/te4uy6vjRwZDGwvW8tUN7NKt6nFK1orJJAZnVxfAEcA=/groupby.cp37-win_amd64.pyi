import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\groupby.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.groupby'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _group_add():
    '\n    Only aggregates on axis=0\n    '
    pass

def _group_mean():
    pass

def _group_ohlc():
    '\n    Only aggregates on axis=0\n    '
    pass

def _group_prod():
    '\n    Only aggregates on axis=0\n    '
    pass

def _group_var():
    pass

_int64_max = 9223372036854775807
def group_add_complex128():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_add_complex64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_add_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_add_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_any_all():
    "\n    Aggregated boolean values to show truthfulness of group elements.\n\n    Parameters\n    ----------\n    out : array of values which this method will write its results to\n    labels : array containing unique label for each group, with its\n        ordering matching up to the corresponding record in `values`\n    values : array containing the truth value of each element\n    mask : array indicating whether a value is na or not\n    val_test : str {'any', 'all'}\n        String object dictating whether to use any or all truth testing\n    skipna : boolean\n        Flag to ignore nan values during truth testing\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object.\n    The returned values will either be 0 or 1 (False or True, respectively).\n    "
    pass

def group_cummax(out, values, labels, ngroups, is_datetimelike):
    '\n    Cumulative maximum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cummax in.\n    values : array\n        Values to take cummax of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    pass

def group_cummin(out, values, labels, ngroups, is_datetimelike):
    '\n    Cumulative minimum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cummin in.\n    values : array\n        Values to take cummin of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    pass

def group_cumprod_float64():
    '\n    Cumulative product of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : float64 array\n        Array to store cumprod in.\n    values : float64 array\n        Values to take cumprod of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        Always false, `values` is never datetime-like.\n    skipna : bool\n        If true, ignore nans in `values`.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    pass

def group_cumsum():
    '\n    Cumulative sum of columns of `values`, in row groups `labels`.\n\n    Parameters\n    ----------\n    out : array\n        Array to store cumsum in.\n    values : array\n        Values to take cumsum of.\n    labels : int64 array\n        Labels to group by.\n    ngroups : int\n        Number of groups, larger than all entries of `labels`.\n    is_datetimelike : bool\n        True if `values` contains datetime-like entries.\n    skipna : bool\n        If true, ignore nans in `values`.\n\n    Notes\n    -----\n    This method modifies the `out` parameter, rather than returning an object.\n    '
    pass

def group_fillna_indexer():
    "\n    Indexes how to fill values forwards or backwards within a group.\n\n    Parameters\n    ----------\n    out : array of int64_t values which this method will write its results to\n        Missing values will be written to with a value of -1\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    mask : array of int64_t values where a 1 indicates a missing value\n    direction : {'ffill', 'bfill'}\n        Direction for fill to be applied (forwards or backwards, respectively)\n    limit : Consecutive values to fill before stopping, or -1 for no limit\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_last():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_max():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_mean_float32():
    pass

def group_mean_float64():
    pass

def group_median_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_min():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_nth():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_ohlc_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_ohlc_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_prod_float32():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_prod_float64():
    '\n    Only aggregates on axis=0\n    '
    pass

def group_quantile(out, labels, values, mask, q, interpolation):
    '\n    Calculate the quantile per group.\n\n    Parameters\n    ----------\n    out : ndarray\n        Array of aggregated values that will be written to.\n    labels : ndarray\n        Array containing the unique group labels.\n    values : ndarray\n        Array containing the values to apply the function against.\n    q : float\n        The quantile value to search for.\n\n    Notes\n    -----\n    Rather than explicitly returning a value, this function modifies the\n    provided `out` parameter.\n    '
    pass

def group_rank():
    "\n    Provides the rank of values within each group.\n\n    Parameters\n    ----------\n    out : array of float64_t values which this method will write its results to\n    values : array of rank_t values to be ranked\n    labels : array containing unique label for each group, with its ordering\n        matching up to the corresponding record in `values`\n    ngroups : int\n        This parameter is not used, is needed to match signatures of other\n        groupby functions.\n    is_datetimelike : bool, default False\n        unused in this method but provided for call compatibility with other\n        Cython transformations\n    ties_method : {'average', 'min', 'max', 'first', 'dense'}, default\n        'average'\n        * average: average rank of group\n        * min: lowest rank in group\n        * max: highest rank in group\n        * first: ranks assigned in order they appear in the array\n        * dense: like 'min', but rank always increases by 1 between groups\n    ascending : boolean, default True\n        False for ranks by high (1) to low (N)\n        na_option : {'keep', 'top', 'bottom'}, default 'keep'\n    pct : boolean, default False\n        Compute percentage rank of data within each group\n    na_option : {'keep', 'top', 'bottom'}, default 'keep'\n        * keep: leave NA values where they are\n        * top: smallest rank if ascending\n        * bottom: smallest rank if descending\n\n    Notes\n    -----\n    This method modifies the `out` parameter rather than returning an object\n    "
    pass

def group_shift_indexer():
    pass

def group_var_float32():
    pass

def group_var_float64():
    pass

def groupsort_indexer():
    '\n    Compute a 1-d indexer.\n\n    The indexer is an ordering of the passed index,\n    ordered by the groups.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        Mappings from group -> position.\n    ngroups: int64\n        Number of groups.\n\n    Returns\n    -------\n    tuple\n        1-d indexer ordered by groups, group counts.\n\n    Notes\n    -----\n    This is a reverse of the label factorization process.\n    '
    pass

def take_2d_axis1_float64_float64():
    pass

tiebreakers = _mod_builtins.dict()
