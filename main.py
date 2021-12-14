import os
from update_docs_pls.updatedocs import UpdateDocs

def main():
    doc_check = UpdateDocs(os.getenv("INPUT_CONFIG_PATH", ".github/UpdateDocs.yaml"))
    doc_check.run()

if __name__ == "__main__":
    main()