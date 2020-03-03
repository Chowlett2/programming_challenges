'''Make a function that returns the SHA-256 secure hash for a given string. 
The hash should be formatted in a hexadecimal digit string.'''

import hashlib
def get_sha256_hash(txt):
    txt = txt.encode()
    return hashlib.sha256(txt).hexdigest()