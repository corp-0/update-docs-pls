class BaseError(Exception):
    pass


class MissingContextInformation(BaseError):
    def __init__(self, info: str):
        super(MissingContextInformation, self).__init__(
            f"We're missing critical information from the context: {info}"
        )