class InvalidPagesValueError(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Pages must be integer, "
                                 f"not {attribute}")


class InvalidYearValueError(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Year must be integer, "
                                 f"not {attribute}")


class InvalidAuthorValueError(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Author must be string, "
                                 f"not {attribute}")


class InvalidNameValueError(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Name must be string, "
                                 f"not {attribute}")


class InvalidPriceValueError(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Price must be float, "
                                 f"not {attribute}")


class InvalidValue(Exception):
    def __init__(self, message="Подано пустое значение"):
        super().__init__(message)


class EmptyLibraryException(Exception):
    def __init__(self, message="Библиотека пуста"):
        super().__init__(message)


class AuthorNotFound(Exception):
    def __init__(self, message="Книга с таким автором не найдена"):
        super().__init__(message)
