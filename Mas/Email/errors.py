class SubjectError(Exception):
   def __init__(self, expression, message=""):
        self.expression = expression
        self.message = f'Invalid subject {expression}' if not message else message
        super().__init__(self.message)


class FileReadingError(Exception):
   def __init__(self, expression, message="", file_name =""):
        self.expression = expression
        self.message = f'Failure reading file {file_name}' if not message else message
        super().__init__(self.message)