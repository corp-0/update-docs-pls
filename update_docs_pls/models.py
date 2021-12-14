from dataclasses import dataclass
from typing import List, Set


@dataclass
class Entry:
    article_name: str
    article_url: str
    files: List[str]


@dataclass
class FileResult:
    filename: str
    url: str


@dataclass
class ArticleResult:
    name: str
    url: str


@dataclass
class Results:
    articles: List[ArticleResult]
    files: List[FileResult]

    def __add__(self, other):
        for article in other.articles:
            if article not in self.articles:
                self.articles.append(article)
        for file in other.files:
            if file not in self.files:
                self.files.append(file)
        return self