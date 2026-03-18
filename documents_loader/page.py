# Now we will interact our ai with a webpage
from langchain_community.document_loaders import WebBaseLoader
url = "https://www.apple.com/macbook-neo/"
data = WebBaseLoader(url)
docs = data.load()
print(docs[0].page_content)
