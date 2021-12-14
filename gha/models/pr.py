from dataclasses import dataclass
from typing import List, Optional
from .user import User
from .repo import Repo
from .file import File
import requests

@dataclass
class Link:
    href: str


@dataclass
class Links:
    self: Link
    html: Link
    issue: Link
    comments: Link
    review_comments: Link
    review_comment: Link
    commits: Link
    statuses: Link


@dataclass
class Reference:
    label: str
    ref: str
    sha: str
    user: User
    repo: Repo


@dataclass
class PR:
    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    number: int
    state: str
    locked: bool
    title: str
    user: User
    body: str
    created_at: str
    updated_at: str
    closed_at: str
    merged_at: str
    merge_commit_sha: str
    assignee: User
    assignees: List[User]
    requested_reviewers: List[User]
    requested_teams: List[User]
    labels: List[str]
    milestone: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    head: Reference
    base: Reference
    _links: Links
    author_association: str
    draft: bool
    merged: bool
    mergeable: bool
    rebaseable: bool
    mergeable_state: str
    merged_by: User
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int
    active_lock_reason: Optional[str] = None
    auto_merge: Optional[any] = None

    def get_files(self) -> List[File]:
        files = []
        url = f"{self.url}/files"
        for file in requests.get(url).json():
            files.append(File(**file))

        return files

