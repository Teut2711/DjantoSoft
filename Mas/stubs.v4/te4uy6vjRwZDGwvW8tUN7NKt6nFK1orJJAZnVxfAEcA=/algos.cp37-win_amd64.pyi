import builtins as _mod_builtins

class Infinity(_mod_builtins.object):
    '\n    Provide a positive Infinity comparison method for ranking.\n    '
    __class__ = Infinity
    __dict__ = {}
    def __eq__(self):
        return False
    
    def __ge__(self):
        return False
    
    def __gt__(self):
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        '\n    Provide a positive Infinity comparison method for ranking.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self):
        return False
    
    def __lt__(self):
        return False
    
    __module__ = 'pandas._libs.algos'
    def __ne__(self):
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class NegInfinity(_mod_builtins.object):
    '\n    Provide a negative Infinity comparison method for ranking.\n    '
    __class__ = NegInfinity
    __dict__ = {}
    def __eq__(self):
        return False
    
    def __ge__(self):
        return False
    
    def __gt__(self):
        return False
    
    __hash__ = None
    def __init__(self, *args, **kwargs):
        '\n    Provide a negative Infinity comparison method for ranking.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self):
        return False
    
    def __lt__(self):
        return False
    
    __module__ = 'pandas._libs.algos'
    def __ne__(self):
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\algos.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.algos'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _validate_limit():
    '\n    Check that the `limit` argument is a positive integer.\n\n    Parameters\n    ----------\n    nobs : int\n    limit : object\n\n    Returns\n    -------\n    int\n        The limit.\n    '
    pass

def backfill():
    pass

def backfill_2d_inplace():
    pass

def backfill_inplace():
    pass

def diff_2d(arr, out, periods, axis):
    pass

def ensure_float32():
    pass

def ensure_float64():
    pass

def ensure_int16():
    pass

def ensure_int32():
    pass

def ensure_int64():
    pass

def ensure_int8():
    pass

def ensure_object():
    pass

def ensure_platform_int():
    pass

def ensure_uint16():
    pass

def ensure_uint32():
    pass

def ensure_uint64():
    pass

def ensure_uint8():
    pass

def groupsort_indexer():
    '\n    Compute a 1-d indexer.\n\n    The indexer is an ordering of the passed index,\n    ordered by the groups.\n\n    Parameters\n    ----------\n    index: int64 ndarray\n        Mappings from group -> position.\n    ngroups: int64\n        Number of groups.\n\n    Returns\n    -------\n    tuple\n        1-d indexer ordered by groups, group counts.\n\n    Notes\n    -----\n    This is a reverse of the label factorization process.\n    '
    pass

def is_lexsorted():
    pass

def is_monotonic(arr, timelike):
    '\n    Returns\n    -------\n    tuple\n        is_monotonic_inc : bool\n        is_monotonic_dec : bool\n        is_unique : bool\n    '
    pass

def kth_smallest(a, k):
    pass

def nancorr():
    pass

def nancorr_spearman():
    pass

def pad():
    pass

def pad_2d_inplace():
    pass

def pad_inplace():
    pass

def rank_1d():
    '\n    Fast NaN-friendly version of ``scipy.stats.rankdata``.\n    '
    pass

def rank_2d():
    '\n    Fast NaN-friendly version of ``scipy.stats.rankdata``.\n    '
    pass

def take_1d_bool_bool():
    pass

def take_1d_bool_object():
    pass

def take_1d_float32_float32():
    pass

def take_1d_float32_float64():
    pass

def take_1d_float64_float64():
    pass

def take_1d_int16_float64():
    pass

def take_1d_int16_int16():
    pass

def take_1d_int16_int32():
    pass

def take_1d_int16_int64():
    pass

def take_1d_int32_float64():
    pass

def take_1d_int32_int32():
    pass

def take_1d_int32_int64():
    pass

def take_1d_int64_float64():
    pass

def take_1d_int64_int64():
    pass

def take_1d_int8_float64():
    pass

def take_1d_int8_int32():
    pass

def take_1d_int8_int64():
    pass

def take_1d_int8_int8():
    pass

def take_1d_object_object():
    pass

def take_2d_axis0_bool_bool():
    pass

def take_2d_axis0_bool_object():
    pass

def take_2d_axis0_float32_float32():
    pass

def take_2d_axis0_float32_float64():
    pass

def take_2d_axis0_float64_float64():
    pass

def take_2d_axis0_int16_float64():
    pass

def take_2d_axis0_int16_int16():
    pass

def take_2d_axis0_int16_int32():
    pass

def take_2d_axis0_int16_int64():
    pass

def take_2d_axis0_int32_float64():
    pass

def take_2d_axis0_int32_int32():
    pass

def take_2d_axis0_int32_int64():
    pass

def take_2d_axis0_int64_float64():
    pass

def take_2d_axis0_int64_int64():
    pass

def take_2d_axis0_int8_float64():
    pass

def take_2d_axis0_int8_int32():
    pass

def take_2d_axis0_int8_int64():
    pass

def take_2d_axis0_int8_int8():
    pass

def take_2d_axis0_object_object():
    pass

def take_2d_axis1_bool_bool():
    pass

def take_2d_axis1_bool_object():
    pass

def take_2d_axis1_float32_float32():
    pass

def take_2d_axis1_float32_float64():
    pass

def take_2d_axis1_float64_float64():
    pass

def take_2d_axis1_int16_float64():
    pass

def take_2d_axis1_int16_int16():
    pass

def take_2d_axis1_int16_int32():
    pass

def take_2d_axis1_int16_int64():
    pass

def take_2d_axis1_int32_float64():
    pass

def take_2d_axis1_int32_int32():
    pass

def take_2d_axis1_int32_int64():
    pass

def take_2d_axis1_int64_float64():
    pass

def take_2d_axis1_int64_int64():
    pass

def take_2d_axis1_int8_float64():
    pass

def take_2d_axis1_int8_int32():
    pass

def take_2d_axis1_int8_int64():
    pass

def take_2d_axis1_int8_int8():
    pass

def take_2d_axis1_object_object():
    pass

def take_2d_multi_bool_bool():
    pass

def take_2d_multi_bool_object():
    pass

def take_2d_multi_float32_float32():
    pass

def take_2d_multi_float32_float64():
    pass

def take_2d_multi_float64_float64():
    pass

def take_2d_multi_int16_float64():
    pass

def take_2d_multi_int16_int16():
    pass

def take_2d_multi_int16_int32():
    pass

def take_2d_multi_int16_int64():
    pass

def take_2d_multi_int32_float64():
    pass

def take_2d_multi_int32_int32():
    pass

def take_2d_multi_int32_int64():
    pass

def take_2d_multi_int64_float64():
    pass

def take_2d_multi_int64_int64():
    pass

def take_2d_multi_int8_float64():
    pass

def take_2d_multi_int8_int32():
    pass

def take_2d_multi_int8_int64():
    pass

def take_2d_multi_int8_int8():
    pass

def take_2d_multi_object_object():
    pass

tiebreakers = _mod_builtins.dict()
def unique_deltas():
    '\n    Efficiently find the unique first-differences of the given array.\n\n    Parameters\n    ----------\n    arr : ndarray[in64_t]\n\n    Returns\n    -------\n    ndarray[int64_t]\n        An ordered ndarray[int64_t]\n    '
    pass

