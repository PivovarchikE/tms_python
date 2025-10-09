class NotIntException(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Attribute must be integer, "
                                 f"not {attribute}")


class NotStrException(Exception):
    def __init__(self, attribute):
        self.attribute = attribute
        Exception.__init__(self, f"Attribute must be string, "
                                 f"not {attribute}")
