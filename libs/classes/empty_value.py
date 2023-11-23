class EmptyValue(Exception):
    """An error for an empty value"""

    def __init__(self, message=None):
        super().__init__(message)
