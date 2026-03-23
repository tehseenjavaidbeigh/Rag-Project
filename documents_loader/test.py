from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
splitter = CharacterTextSplitter(
    separator = "",
    chunk_size = 10,
    chunk_overlap = 1
)
data = TextLoader("documents_loader/data.txt")

docs = data.load()
# print(docs)
chunks = splitter.split_documents(docs)
# print(docs[0])

# print(len(docs))

print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()
    print()
    print()