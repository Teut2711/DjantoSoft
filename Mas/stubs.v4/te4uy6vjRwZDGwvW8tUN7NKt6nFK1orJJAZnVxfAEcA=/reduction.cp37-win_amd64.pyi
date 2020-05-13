import builtins as _mod_builtins
import distutils.version as _mod_distutils_version

class BlockSlider(_mod_builtins.object):
    '\n    Only capable of sliding on axis=0\n    '
    __class__ = BlockSlider
    def __init__(self, *args, **kwargs):
        '\n    Only capable of sliding on axis=0\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def blocks(self):
        pass
    
    @property
    def dummy(self):
        pass
    
    @property
    def frame(self):
        pass
    
    @property
    def idx_slider(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def nblocks(self):
        pass
    

class InvalidApply(_mod_builtins.Exception):
    __class__ = InvalidApply
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'pandas._libs.reduction'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

LooseVersion = _mod_distutils_version.LooseVersion
class Reducer(_mod_builtins.object):
    '\n    Performs generic reduction operation on a C or Fortran-contiguous ndarray\n    while avoiding ndarray construction overhead\n    '
    __class__ = Reducer
    def __init__(self, *args, **kwargs):
        '\n    Performs generic reduction operation on a C or Fortran-contiguous ndarray\n    while avoiding ndarray construction overhead\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def get_result(self):
        pass
    

class SeriesBinGrouper(_BaseGrouper):
    '\n    Performs grouping operation according to bin edges, rather than labels\n    '
    __class__ = SeriesBinGrouper
    def __init__(self, *args, **kwargs):
        '\n    Performs grouping operation according to bin edges, rather than labels\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def arr(self):
        pass
    
    @property
    def bins(self):
        pass
    
    @property
    def dummy_arr(self):
        pass
    
    @property
    def dummy_index(self):
        pass
    
    @property
    def f(self):
        pass
    
    def get_result(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def ityp(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def typ(self):
        pass
    
    @property
    def values(self):
        pass
    

class SeriesGrouper(_BaseGrouper):
    '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
    __class__ = SeriesGrouper
    def __init__(self, *args, **kwargs):
        '\n    Performs generic grouping operation while avoiding ndarray construction\n    overhead\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def arr(self):
        pass
    
    @property
    def dummy_arr(self):
        pass
    
    @property
    def dummy_index(self):
        pass
    
    @property
    def f(self):
        pass
    
    def get_result(self):
        pass
    
    @property
    def index(self):
        pass
    
    @property
    def ityp(self):
        pass
    
    @property
    def labels(self):
        pass
    
    @property
    def name(self):
        pass
    
    @property
    def typ(self):
        pass
    
    @property
    def values(self):
        pass
    

class Slider(_mod_builtins.object):
    '\n    Only handles contiguous data for now\n    '
    __class__ = Slider
    def __init__(self, *args, **kwargs):
        '\n    Only handles contiguous data for now\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _BaseGrouper(_mod_builtins.object):
    __class__ = _BaseGrouper
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\dell\\appdata\\local\\pypoetry\\cache\\virtualenvs\\somework-4urmfaer-py3.7\\Lib\\site-packages\\pandas\\_libs\\reduction.cp37-win_amd64.pyd'
__name__ = 'pandas._libs.reduction'
__package__ = 'pandas._libs'
def __pyx_unpickle_Enum():
    pass

def __pyx_unpickle_Reducer():
    pass

def __pyx_unpickle_SeriesBinGrouper():
    pass

def __pyx_unpickle_SeriesGrouper():
    pass

def __pyx_unpickle_Slider():
    pass

def __pyx_unpickle__BaseGrouper():
    pass

__test__ = _mod_builtins.dict()
def apply_frame_axis0():
    pass

def compute_reduction():
    '\n\n    Parameters\n    -----------\n    arr : np.ndarray\n    f : function\n    axis : integer axis\n    dummy : type of reduced output (series)\n    labels : Index or None\n    '
    pass

def copy(x):
    "Shallow copy operation on arbitrary Python objects.\n\n    See the module's __doc__ string for more info.\n    "
    pass

def is_scalar():
    '\n    Parameters\n    ----------\n    val : object\n        This includes:\n\n        - numpy array scalar (e.g. np.int64)\n        - Python builtin numerics\n        - Python builtin byte arrays and strings\n        - None\n        - datetime.datetime\n        - datetime.timedelta\n        - Period\n        - decimal.Decimal\n        - Interval\n        - DateOffset\n        - Fraction\n        - Number.\n\n    Returns\n    -------\n    bool\n        Return True if given object is scalar.\n\n    Examples\n    --------\n    >>> dt = datetime.datetime(2018, 10, 3)\n    >>> pd.api.types.is_scalar(dt)\n    True\n\n    >>> pd.api.types.is_scalar([2, 3])\n    False\n\n    >>> pd.api.types.is_scalar({0: 1, 2: 3})\n    False\n\n    >>> pd.api.types.is_scalar((0, 2))\n    False\n\n    pandas supports PEP 3141 numbers:\n\n    >>> from fractions import Fraction\n    >>> pd.api.types.is_scalar(Fraction(3, 5))\n    True\n    '
    pass

def maybe_convert_objects():
    '\n    Type inference function-- convert object array to proper dtype\n\n    Parameters\n    ----------\n    values : ndarray\n        Array of object elements to convert.\n    try_float : bool, default False\n        If an array-like object contains only float or NaN values is\n        encountered, whether to convert and return an array of float dtype.\n    safe : bool, default False\n        Whether to upcast numeric type (e.g. int cast to float). If set to\n        True, no upcasting will be performed.\n    convert_datetime : bool, default False\n        If an array-like object contains only datetime values or NaT is\n        encountered, whether to convert and return an array of M8[ns] dtype.\n    convert_timedelta : bool, default False\n        If an array-like object contains only timedelta values or NaT is\n        encountered, whether to convert and return an array of m8[ns] dtype.\n    convert_to_nullable_integer : bool, default False\n        If an array-like object contains only interger values (and NaN) is\n        encountered, whether to convert and return an IntegerArray.\n\n    Returns\n    -------\n    Array of converted object values to more specific dtypes if applicable.\n    '
    pass

