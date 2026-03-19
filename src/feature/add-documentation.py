```python
# src/feature/add-documentation.py

class Documentation:

    def __init__(self):
        self.documents = []

    def add_document(self, title, content):
        document = {
            'title': title,
            'content': content
        }
        self.documents.append(document)

    def get_document(self, title):
        for document in self.documents:
            if document['title'] == title:
                return document
        return None

    def update_document(self, title, new_content):
        for document in self.documents:
            if document['title'] == title:
                document['content'] = new_content
                return document
        return None

    def delete_document(self, title):
        for index, document in enumerate(self.documents):
            if document['title'] == title:
                del self.documents[index]
                return True
        return False

    def list_documents(self):
        return self.documents
```