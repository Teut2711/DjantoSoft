import builtins as _mod_builtins

class HASH(_mod_builtins.object):
    'A hash is an object used to calculate a checksum of a string of information.\n\nMethods:\n\nupdate() -- updates the current digest with an additional string\ndigest() -- return the current digest value\nhexdigest() -- return the current digest as a string of hexadecimal digits\ncopy() -- return a copy of the current hash object\n\nAttributes:\n\nname -- the hash algorithm being used by this object\ndigest_size -- number of bytes in this hashes output'
    __class__ = HASH
    def __init__(self, *args, **kwargs):
        'A hash is an object used to calculate a checksum of a string of information.\n\nMethods:\n\nupdate() -- updates the current digest with an additional string\ndigest() -- return the current digest value\nhexdigest() -- return the current digest as a string of hexadecimal digits\ncopy() -- return a copy of the current hash object\n\nAttributes:\n\nname -- the hash algorithm being used by this object\ndigest_size -- number of bytes in this hashes output'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def block_size(self):
        pass
    
    def copy(self):
        'Return a copy of the hash object.'
        pass
    
    def digest(self):
        'Return the digest value as a bytes object.'
        pass
    
    @property
    def digest_size(self):
        pass
    
    def hexdigest(self):
        'Return the digest value as a string of hexadecimal digits.'
        pass
    
    @property
    def name(self):
        pass
    
    def update(self, obj):
        "Update this hash object's state with the provided string."
        pass
    

__doc__ = None
__file__ = 'c:\\python38\\dlls\\_hashlib.pyd'
__name__ = '_hashlib'
__package__ = ''
def hmac_digest(key, msg, digest):
    'Single-shot HMAC.'
    pass

def new(name, string):
    'Return a new hash object using the named algorithm.\n\nAn optional string argument may be provided and will be\nautomatically hashed.\n\nThe MD5 and SHA1 algorithms are always supported.'
    pass

def openssl_md5(string):
    'Returns a md5 hash object; optionally initialized with a string'
    pass

openssl_md_meth_names = _mod_builtins.frozenset()
def openssl_sha1(string):
    'Returns a sha1 hash object; optionally initialized with a string'
    pass

def openssl_sha224(string):
    'Returns a sha224 hash object; optionally initialized with a string'
    pass

def openssl_sha256(string):
    'Returns a sha256 hash object; optionally initialized with a string'
    pass

def openssl_sha384(string):
    'Returns a sha384 hash object; optionally initialized with a string'
    pass

def openssl_sha512(string):
    'Returns a sha512 hash object; optionally initialized with a string'
    pass

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen):
    'Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as pseudorandom function.'
    pass

def scrypt(password):
    'scrypt password-based key derivation function.'
    pass

