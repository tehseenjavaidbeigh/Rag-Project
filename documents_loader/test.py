from langchain_community.document_loaders import TextLoader
data = TextLoader("documents_loader/data.txt")
docs = data.load()
# print(docs)

# print(docs[0])

print(docs[0].page_content)

