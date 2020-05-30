
import mimetypes
from Email.errors import FileReadingError


def read_html(file_name, mode):
    try:
        import codecs
        with codecs.open(file_name) as f:
            return f.read()
    except FileNotFoundError:
        pass
    except:
        raise FileReadingError(f"Error in reading {file_name} file")


def read_file(file_name, mode, return_mime=False):
    try:
        with open(file_name, mode) as f:
            if return_mime:
                return (f.read(), mimetypes.guess_type(file_name)[0])
            else:
                return f.read()
    except FileNotFoundError:
        pass
    except:
        raise FileReadingError(f"Error in reading {file_name} file")
