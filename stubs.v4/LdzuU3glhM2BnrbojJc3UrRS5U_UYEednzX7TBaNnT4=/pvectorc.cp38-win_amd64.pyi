import builtins as _mod_builtins

class PVector(_mod_builtins.object):
    'Persistent vector'
    def __add__(self, value):
        'Return self+value.'
        return PVector()
    
    __class__ = PVector
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        'Persistent vector'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return PVector()
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return PVector()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        'Pickle support method'
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return PVector()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def append(self):
        'Appends an element'
        pass
    
    def count(self):
        'Return number of occurrences of value'
        pass
    
    def delete(self):
        'Delete element(s) by index'
        pass
    
    def evolver(self):
        'Return new evolver for pvector'
        pass
    
    def extend(self):
        'Extend'
        pass
    
    def index(self):
        'Return first index of value'
        pass
    
    def mset(self):
        'Inserts multiple elements at the specified positions'
        pass
    
    def remove(self):
        'Remove element(s) by equality'
        pass
    
    def set(self):
        'Inserts an element at the specified position'
        pass
    
    def tolist(self):
        'Convert to list'
        pass
    
    def transform(self):
        'Apply one or more transformations'
        pass
    

__doc__ = 'Persistent vector'
__file__ = 'c:\\python38\\lib\\site-packages\\pvectorc.cp38-win_amd64.pyd'
__name__ = 'pvectorc'
__package__ = ''
def pvector(iterable=None):
    'pvector([iterable])\nCreate a new persistent vector containing the elements in iterable.\n\n>>> v1 = pvector([1, 2, 3])\n>>> v1\npvector([1, 2, 3])'
    pass

