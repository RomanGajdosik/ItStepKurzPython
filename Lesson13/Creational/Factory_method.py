class Document:
    def create(self):
        raise NotImplementedError("Metóda create() musí byť prepísaná.")

class PDFDocument(Document):
    def create(self):
        return "Vytváram PDF dokument."

class WordDocument(Document):
    def create(self):
        return "Vytváram Word dokument."

class Factory:
    def create_document(self, type):
        if type == 'pdf':
            return PDFDocument()
        elif type == 'word':
            return WordDocument()
        else:
            raise ValueError("Neznámy typ dokumentu")

factory = Factory()
pdf = factory.create_document('pdf')
print(pdf.create())

word = factory.create_document('word')
print(word.create())
