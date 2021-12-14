import json
import os

from .exceptions import MissingContextInformation
from .models.action import PullRequestAction
from .models.pr import PR
from .models.repo import Repo
from .models.user import User


def read_payload():
    file = os.getenv("GITHUB_EVENT_PATH")
    if file is None:
        raise MissingContextInformation("path to github payload file")

    with open(file, 'r', encoding='UTF-8') as f:
        return json.load(f)


def try_get_pull_request_action(payload: dict):
    if not payload.get("pull_request"):
        raise NotImplementedError("action type is not yet implemented!")
    action = PullRequestAction(**payload)

    pull_request = PR(**payload["pull_request"])
    repository = Repo(**payload["repository"])
    sender = User(**payload["sender"])

    action.pull_request = pull_request
    action.repository = repository
    action.sender = sender
    return action


class Context:
    def __init__(self):
        self.payload = read_payload()
        self.action = try_get_pull_request_action(self.payload)

