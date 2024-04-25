class Blob:
    """wraps a string that
       we got by reading a file.
    """
    def __init__(self, data):
        self._oid = None
        self.data = data

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value

    def type(self):
        return "blob"

    def __str__(self):
        """serialise each object we store.

        Returns:
            _type_: _description_
        """
        return self.data
