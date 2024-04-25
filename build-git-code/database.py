import hashlib
import zlib
import os
import random
import string


class Database:
    """stores all our content away in .git/objects. Its
       job for the time being is to take this Blob object we have constructed and store it on disk according
       to the Git database format.
    """ 
    def __init__(self, pathname):
        self.pathname = pathname
    

    def store(self, object):
        # obj_string = str(object).encode("ascii")
        obj_string = str(object).encode("utf-8")
        content = f"{object.type} {len(obj_string)} {obj_string}"
        
        object.oid = hashlib.sha1(content.encode('utf-8')).hexdigest()
        self.write_object(object.oid, content)

    def write_object(self, oid, content):
        object_path = os.path.join(self.pathname, oid[0:2], oid[2:])
        dirname = os.path.dirname(object_path)
        temp_path = os.path.join(dirname, self.generate_temp_name())

        try:
            flags = os.O_RDWR | os.O_CREAT | os.O_EXCL
            file = os.open(temp_path, flags)
        except FileNotFoundError:
            os.mkdir(dirname)
            file = os.open(temp_path, flags)
        
        deflate_level = zlib.Z_BEST_SPEED
        compressed = zlib.compress(content.encode('utf-8'), level=deflate_level)

        os.write(file, compressed)
        os.close(file)

        os.rename(temp_path, object_path)

    def generate_temp_name(self):
        TEMP_CHARS = string.ascii_letters + string.digits
        return "tmp_obj_" + "".join(random.choices(TEMP_CHARS, k=6))