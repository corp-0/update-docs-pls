# UpdateDocsPls

Silly little github action job to remind contributors to update docs.

## Usage

Add the job to your github workflow.

Example:
```yaml
name: UpdateDocsPls
on:
    pull_request:
        branches:
            - master
        types:
            - opened
            - edited
jobs:
    check_docs:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              
            - name: DocsReminder
              uses: corp-0/update-docs-pls@master
              id: DocsReminder
              
            - name: Comment PR
              if: ${{ steps.DocsReminder.outputs.found_doc_related_changes == 1}}
              uses: thollander/actions-comment-pull-request@v1
              with:
                message: ${{ steps.DocsReminder.outputs.comment_content }}
                GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Configuration
The action is configured by adding a UpdateDocsPls.yaml file to .github folder. Alternatively, you can set the path to 
the configuration file using the input ``config_path`` in your workflow.

The configuration must look something like this:
```yaml
entries:
    - article_name: "Name of your documentation article"
      article_url: "URL to your documentation article"
      files:
          - "path/to/file.md"
          - "path/*.md" # wildcards allowed
          - "**/*.jpg" # recursive wildcards allowed
```
add as many entries as your project requires.
