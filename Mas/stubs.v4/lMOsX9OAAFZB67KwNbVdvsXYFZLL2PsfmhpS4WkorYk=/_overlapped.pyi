import builtins as _mod_builtins

def BindLocal(handle, family):
    'BindLocal(handle, family) -> None\n\nBind a socket handle to an arbitrary local port.\nfamily should AF_INET or AF_INET6.\n'
    pass

def ConnectPipe(addr):
    'ConnectPipe(addr) -> pipe_handle\n\nConnect to the pipe for asynchronous I/O (overlapped).'
    pass

def CreateEvent(EventAttributes, ManualReset, InitialState, Name):
    'CreateEvent(EventAttributes, ManualReset, InitialState, Name) -> Handle\n\nCreate an event.  EventAttributes must be None.\n'
    pass

def CreateIoCompletionPort(handle, port, key, concurrency):
    'CreateIoCompletionPort(handle, port, key, concurrency) -> port\n\nCreate a completion port or register a handle with a port.'
    pass

ERROR_IO_PENDING = 997
ERROR_NETNAME_DELETED = 64
ERROR_OPERATION_ABORTED = 995
ERROR_PIPE_BUSY = 231
ERROR_SEM_TIMEOUT = 121
def FormatMessage(error_code):
    'FormatMessage(error_code) -> error_message\n\nReturn error message for an error code.'
    pass

def GetQueuedCompletionStatus(port, msecs):
    'GetQueuedCompletionStatus(port, msecs) -> (err, bytes, key, address)\n\nGet a message from completion port.  Wait for up to msecs milliseconds.'
    return tuple()

INFINITE = 4294967295
INVALID_HANDLE_VALUE = 18446744073709551615
NULL = 0
class Overlapped(_mod_builtins.object):
    'OVERLAPPED structure wrapper'
    def AcceptEx(self, listen_handle, accept_handle):
        'AcceptEx(listen_handle, accept_handle) -> Overlapped[address_as_bytes]\n\nStart overlapped wait for client to connect'
        pass
    
    def ConnectEx(self, client_handle, address_as_bytes):
        'ConnectEx(client_handle, address_as_bytes) -> Overlapped[None]\n\nStart overlapped connect.  client_handle should be unbound.'
        pass
    
    def ConnectNamedPipe(self, handle):
        'ConnectNamedPipe(handle) -> Overlapped[None]\n\nStart overlapped wait for a client to connect.'
        pass
    
    def DisconnectEx(self, handle, flags):
        'DisconnectEx(handle, flags) -> Overlapped[None]\n\nStart overlapped connect.  client_handle should be unbound.'
        pass
    
    def ReadFile(self, handle, size):
        'ReadFile(handle, size) -> Overlapped[message]\n\nStart overlapped read'
        pass
    
    def ReadFileInto(self, handle, buf):
        'ReadFileInto(handle, buf) -> Overlapped[bytes_transferred]\n\nStart overlapped receive'
        pass
    
    def TransmitFile(self, socket, file, offset, offset_high, count_to_write, count_per_send, flags):
        'TransmitFile(socket, file, offset, offset_high, count_to_write, count_per_send, flags) -> Overlapped[None]\n\nTransmit file data over a connected socket.'
        pass
    
    def WSARecv(self):
        'RecvFile(handle, size, flags) -> Overlapped[message]\n\nStart overlapped receive'
        pass
    
    def WSARecvInto(self, handle, buf, flags):
        'WSARecvInto(handle, buf, flags) -> Overlapped[bytes_transferred]\n\nStart overlapped receive'
        pass
    
    def WSASend(self, handle, buf, flags):
        'WSASend(handle, buf, flags) -> Overlapped[bytes_transferred]\n\nStart overlapped send'
        pass
    
    def WriteFile(self, handle, buf):
        'WriteFile(handle, buf) -> Overlapped[bytes_transferred]\n\nStart overlapped write'
        pass
    
    __class__ = Overlapped
    def __init__(self, *args, **kwargs):
        'OVERLAPPED structure wrapper'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def address(self):
        'Address of overlapped structure'
        pass
    
    def cancel(self):
        'cancel() -> None\n\nCancel overlapped operation'
        pass
    
    @property
    def error(self):
        'Error from last operation'
        pass
    
    @property
    def event(self):
        'Overlapped event handle'
        pass
    
    def getresult(self, wait=False):
        'getresult(wait=False) -> result\n\nRetrieve result of operation.  If wait is true then it blocks\nuntil the operation is finished.  If wait is false and the\noperation is still pending then an error is raised.'
        pass
    
    @property
    def pending(self):
        'Whether the operation is pending'
        pass
    

def PostQueuedCompletionStatus(port, bytes, key, address):
    'PostQueuedCompletionStatus(port, bytes, key, address) -> None\n\nPost a message to completion port.'
    pass

def RegisterWaitWithQueue(Object, CompletionPort, Overlapped, Timeout):
    'RegisterWaitWithQueue(Object, CompletionPort, Overlapped, Timeout)\n    -> WaitHandle\n\nRegister wait for Object; when complete CompletionPort is notified.\n'
    pass

def ResetEvent(Handle):
    'ResetEvent(Handle) -> None\n\nReset event.\n'
    pass

SO_UPDATE_ACCEPT_CONTEXT = 28683
SO_UPDATE_CONNECT_CONTEXT = 28688
def SetEvent(Handle):
    'SetEvent(Handle) -> None\n\nSet event.\n'
    pass

TF_REUSE_SOCKET = 2
def UnregisterWait(WaitHandle):
    'UnregisterWait(WaitHandle) -> None\n\nUnregister wait handle.\n'
    pass

def UnregisterWaitEx(WaitHandle, Event):
    'UnregisterWaitEx(WaitHandle, Event) -> None\n\nUnregister wait handle.\n'
    pass

__doc__ = None
__file__ = 'c:\\python37\\dlls\\_overlapped.pyd'
__name__ = '_overlapped'
__package__ = ''
