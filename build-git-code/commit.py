class Commit:
    def __init__(self, tree, author, message):
        self.tree = tree
        self.author = author
        self.message = message
    
    def type(self):
        return "commit"
    
    def __str__(self):
        lines = [
            f"tree {self.tree}",
            f"author {self.author}",
            f"committer {self.author}",
            "",
            self.message
        ]

        return "/n".join(lines)
    