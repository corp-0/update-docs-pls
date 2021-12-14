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
    pull_request: PR
    changes: Optional[dict] = None
    before: Optional[dict] = None
    after: Optional[dict] = None

    def get_files(self) -> List[File]:
        return self.pull_request.get_files()