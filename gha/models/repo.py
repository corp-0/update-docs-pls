from dataclasses import dataclass
from .user import User
from typing import Optional

@dataclass
class Repo:
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: User
    html_url: str
    description: str
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    forks_count: int
    mirror_url: str
    archived: bool
    disabled: bool
    open_issues_count: int
    license: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str
    allow_squash_merge: Optional[any] = None
    allow_merge_commit: Optional[any] = None
    allow_rebase_merge: Optional[any] = None
    delete_branch_on_merge: Optional[any] = None
    allow_forking: Optional[any] = None
    is_template: Optional[any] = None
    topics: Optional[any] = None
    visibility: Optional[any] = None
    web_commit_signoff_required: Optional[any] = None