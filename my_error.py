class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"My custom Error: {sefl.message}"
