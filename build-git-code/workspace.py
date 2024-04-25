import os

class Workspace:
    IGNORE = [".", "..", ".git", "__pycache__"]

    def __init__(self, pathname):
        self.pathname = pathname

    def list_files(self):
        return [filename for filename in os.listdir(self.pathname) if filename not in self.IGNORE]
    
    def read_file(self, path):
        """ a method to read the contents of a file
            The result of this method will be passed into a Blob object

        Args:
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        with open(os.path.join(self.pathname, path), "r") as file:
            return file.read()

