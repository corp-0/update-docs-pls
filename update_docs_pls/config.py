from typing import List
from yaml import safe_load
from .exceptions import MissingConfigurationFile, InvalidConfigurationFile
from .models import Entry

class Config:
    entries: List[Entry]

    def __init__(self, path: str):
        try:
            if path is None:
                raise MissingConfigurationFile(str(path))
            with open(path, 'r') as f:
                data = safe_load(f)
        except FileNotFoundError:
            raise MissingConfigurationFile(path)
        self.get_entries(data)

    def get_entries(self, data: dict):
        if "entries" not in data:
            raise InvalidConfigurationFile('Missing entries')
        self.entries = [Entry(**entry) for entry in data["entries"]]
