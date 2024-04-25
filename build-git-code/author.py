class Author:
    def __init__(self, name, email, time):
        self.name = name
        self.email = email
        self.time = time
    def __str__(self):
        timestamp = self.time.strftime("%s %z")
        return f"{self.name} <{self.email}> {timestamp}"