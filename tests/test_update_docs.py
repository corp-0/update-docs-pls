import os
import unittest
from update_docs_pls.updatedocs import UpdateDocs
from  update_docs_pls.models import Results, FileResult, ArticleResult, Entry

os.environ["GITHUB_EVENT_PATH"] = "data/pr.json"

class TestFileMatching(unittest.TestCase):
    def setUp(self) -> None:
        self.update_docs = UpdateDocs("data/test_config.yaml")

    def test_given_a_pattern_return_matching_result(self):
        files = [FileResult("pr2changelog/context.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/context.py")]
        articles = [ArticleResult("Context", "https://my-wiki/context")]
        expected_results = Results(articles, files)
        entry = Entry("Context", "https://my-wiki/context", ["pr2changelog/context.py"])

        self.assertEqual(expected_results, self.update_docs.match_files(entry))

    def test_given_a_pattern_with_wildcard_return_all_matching_results(self):
        files = [
            FileResult("tests/test_change.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_change.py"),
            FileResult("tests/test_context.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_context.py")
        ]
        articles = [ArticleResult("Test", "https://my-wiki/tests")]
        expected_results = Results(articles, files)
        entry = Entry("Test", "https://my-wiki/tests", ["tests/**"])

        self.assertEqual(expected_results, self.update_docs.match_files(entry))

    def test_given_a_non_matching_pattern_return_none(self):
        entry = Entry("Non-matching", "https://my-wiki/non-matching", ["**/non-matching.txt"])

        self.assertIsNone(self.update_docs.match_files(entry))

    def test_given_a_pattern_with_multiple_wildcards_return_all_matching_results(self):
        files = [
            FileResult("pr2changelog/context.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/context.py"),
            FileResult("pr2changelog/document.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/document.py"),
            FileResult("pr2changelog/pr.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/pr.py"),
            FileResult("tests/test_change.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_change.py"),
            FileResult("tests/test_context.py", "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_context.py")
        ]
        articles = [ArticleResult("Python", "https://my-wiki/py")]
        expected_results = Results(articles, files)
        entry = Entry("Python", "https://my-wiki/py", ["**/*.py"])

        self.assertEqual(expected_results, self.update_docs.match_files(entry))

    def test_a_whole_run(self):
        articles = [
            ArticleResult("Context", "https://my-wiki/context"),
            ArticleResult("Tests", "https://my-wiki/tests"),
            ArticleResult("Python", "https://my-wiki/py")
        ]

        files = [
            FileResult("pr2changelog/context.py",
                       "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/context.py"),
            FileResult("tests/test_change.py",
                       "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_change.py"),
            FileResult("tests/test_context.py",
                       "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/tests/test_context.py"),
            FileResult("pr2changelog/document.py",
                       "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/document.py"),
            FileResult("pr2changelog/pr.py",
                       "https://github.com/corp-0/pr2changelog/blob/946ac02359884a18c3327f9eabbd060959c39b0f/pr2changelog/pr.py")
        ]

        expected_results = Results(articles, files)
        self.assertEqual(expected_results, self.update_docs.run())

