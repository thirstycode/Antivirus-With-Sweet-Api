import hashlib

# finding md5 hash of file

def md5(file_loc):
    try:
        hasher = hashlib.md5()
        with open(file_loc, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except PermissionError:
        pass                                   #you can change this or improve this with your need
    except MemoryError:
        pass                                   #you can change this or improve this with your need
