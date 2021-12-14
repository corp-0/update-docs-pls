from dataclasses import dataclass
from typing import List, Optional
from .user import User
from .repo import Repo
from .pr import PR
from .file import File

@dataclass
class Action:
    action: str
    sender: User
    repository: Repo


@dataclass
class PullRequestAction(Action):
    number: int
    # changes: Optional[dict]
    pull_request: PR

    def get_files(self) -> List[File]:
        return self.pull_request.get_files()