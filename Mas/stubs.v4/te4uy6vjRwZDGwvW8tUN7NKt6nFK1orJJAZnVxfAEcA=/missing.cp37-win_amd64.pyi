import builtins as _mod_builtins

class C_NAType(_mod_builtins.object):
    __class__ = C_NAType
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

NA = NAType()
class NAType(C_NAType):
    '\n    NA ("not available") missing value indicator.\n\n    .. warning::\n\n       Experimental: the behaviour of NA can still change without warning.\n\n    .. versionadded:: 1.0.0\n\n    The NA singleton is a missing value indicator defined by pandas. It is\n    used in certain new extension dtypes (currently the "string" dtype).\n    '
    _HANDLED_TYPES = _mod_builtins.tuple()
    def __abs__(self):
        return NAType()
    
    def __add__(self, other):
        return NAType()
    
    def __and__(self, other):
        return NAType()
    
    __array_priority__ = 1000
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        pass
    
    def __bool__(self):
        return False
    
    __class__ = NAType
    __dict__ = {}
    def __divmod__(self, other):
        return (0, 0)
    
    def __eq__(self, other):
        return False
    
    def __floordiv__(self, other):
        return 0
    
    def __ge__(self, other):
        return False
    
    def __gt__(self, other):
        return False
    
    def __hash__(self):
        return 0
    
    def __init__(self, *args, **kwargs):
        '\n    NA ("not available") missing value indicator.\n\n    .. warning::\n\n       Experimental: the behaviour of NA can still change without warning.\n\n    .. versionadded:: 1.0.0\n\n    The NA singleton is a missing value indicator defined by pandas. It is\n    used in certain new extension dtypes (currently the "string" dtype).\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __invert__(self):
        return NAType()
    
    def __le__(self, other):
        return False
    
    def __lt__(self, other):
        return False
    
    def __matmul__(self, other):
        pass
    
    def __mod__(self, other):
        return NAType()
    
    def __mul__(self, other):
        return NAType()
    
    def __ne__(self, other):
        return False
    
    def __neg__(self):
        return NAType()
    
    def __or__(self, other):
        return NAType()
    
    def __pos__(self):
        return NAType()
    
    def __pow__(self, other):
        return NAType()
    
    def __radd__(self, other):
        return NAType()
    
    def __rand__(self, other):
        return NAType()
    
    def __rdivmod__(self, other):
        return (0, 0)
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        return 'unicode'
    
    def __rfloordiv__(self, other):
        return NAType()
    
    def __rmatmul__(self, other):
        pass
    
    def __rmod__(self, other):
        return NAType()
    
    def __rmul__(self, other):
        return NAType()
    
    def __ror__(self, other):
        return NAType()
    
    def __rpow__(self, other):
        return NAType()
    
    def __rsub__(self, other):
        return NAType()
    
    def __rtruediv__(self, other):
        return NAType()
    
    def __rxor__(self, other):
        return NAType()
    
    def __sub__(self, other):
        return NAType()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, other):
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def __xor__(self, other):
        return NAType()
    
    _instance = NAType()

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\missing.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.missing'
__package__ = 'pandas._libs'
__pyx_capi__ = _mod_builtins.dict()
def __pyx_unpickle_C_NAType():
    pass

__test__ = _mod_builtins.dict()
def _create_binary_propagating_op():
    pass

def _create_unary_propagating_op():
    pass

def checknull():
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def checknull_old():
    '\n    Return boolean describing of the input is NA-like, defined here as any\n    of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    val : object\n\n    Returns\n    -------\n    result : bool\n\n    Notes\n    -----\n    The difference between `checknull` and `checknull_old` is that `checknull`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def is_platform_32bit():
    '\n    Checking if the running platform is 32-bit.\n\n    Returns\n    -------\n    bool\n        True if the running platform is 32-bit.\n    '
    return bool

def isnaobj():
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    pass

def isnaobj2d():
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull`:\n     - None\n     - nan\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def isnaobj2d_old():
    '\n    Return boolean mask denoting which elements of a 2-D array are na-like,\n    according to the criteria defined in `checknull_old`:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n     - np.datetime64 representation of NaT\n     - np.timedelta64 representation of NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n\n    Notes\n    -----\n    The difference between `isnaobj2d` and `isnaobj2d_old` is that `isnaobj2d`\n    does *not* consider INF or NEGINF to be NA.\n    '
    pass

def isnaobj_old():
    '\n    Return boolean mask denoting which elements of a 1-D array are na-like,\n    defined as being any of:\n     - None\n     - nan\n     - INF\n     - NEGINF\n     - NaT\n\n    Parameters\n    ----------\n    arr : ndarray\n\n    Returns\n    -------\n    result : ndarray (dtype=np.bool_)\n    '
    pass

def isneginf_scalar():
    pass

def isposinf_scalar():
    pass

def maybe_dispatch_ufunc_to_dunder_op():
    "\n    Dispatch a ufunc to the equivalent dunder method.\n\n    Parameters\n    ----------\n    self : ArrayLike\n        The array whose dunder method we dispatch to\n    ufunc : Callable\n        A NumPy ufunc\n    method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}\n    inputs : ArrayLike\n        The input arrays.\n    kwargs : Any\n        The additional keyword arguments, e.g. ``out``.\n\n    Returns\n    -------\n    result : Any\n        The result of applying the ufunc\n    "
    pass

