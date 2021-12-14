class BaseError(Exception):
    pass

class MissingConfigurationFile(BaseError):
    def __init__(self, path: str):
        super().__init__(f"Configuration file couldn't be found at given path: {path}")

class InvalidConfigurationFile(BaseError):
    def __init__(self, key: str):
        super().__init__(f"Configuration is invalid, missing required key: {key}")