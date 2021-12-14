import fnmatch
from typing import Optional

from gha.context import Context
from .config import Config
from .models import Results, FileResult, ArticleResult, Entry
from actions_toolkit import core
from .message import Messager

class UpdateDocs:
    def __init__(self, path: str):
        self.config = Config(path)
        self.context = Context()

    def match_files(self, entry: Entry) -> Optional[Results]:
        """Try to match the entry to changed files in a PR. Returns None if no match was found."""
        articles = [ArticleResult(entry.article_name, entry.article_url)]
        files = []
        changed_files = self.context.action.get_files()

        for file in changed_files:
            for pattern in entry.files:
                if not fnmatch.fnmatch(file.filename, pattern):
                    continue
                files.append(FileResult(file.filename, file.blob_url))

        if files:
            results = Results(articles, files)
            return results
        return None

    def produce_output(self, results: Results):
        messager = Messager(results)
        messager.compose()
        core.info("Produced output")
        core.info(messager.message)
        core.set_output("comment_content", messager.message)

    def run(self) -> Optional[Results]:
        final_result= Results([], [])
        for entry in self.config.entries:
            result = self.match_files(entry)
            if not result is None:
                final_result += result

        if final_result.files and final_result.articles:
            core.info("Found matching files and articles")
            core.set_output("found_doc_related_changes", True)
            self.produce_output(final_result)
            return final_result
        core.set_output("found_doc_related_changes", False)
        return None
