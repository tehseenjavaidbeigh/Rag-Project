from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import TokenTextSplitter

load_dotenv()

splitter = TokenTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10
)

data = PyPDFLoader("documents_loader/dataset.pdf")
docs = data.load()
# model = ChatMistralAI(model = "mistral-small-2506")
# template =ChatPromptTemplate.from_messages(
#     [("system","You are an AI that summarises the text"),
#      ("human","{data}")])

# prompt = template.format_messages(data = docs[0].page_content) # if we just write docs.page_content then it will give us error as in case of pdf we have many pages and each page has its own meta data na page content. Therefore we have to accurately specify the page_content of which page we want to summarise

# result = model.invoke(prompt)
# print(result.content)
#unlike text file pdf will not have length of 1



chunks = splitter.split_documents(docs)
print(len(chunks))
for i in chunks:
    print(i.page_content)
    print()
    print()
    print()
    print()
    print()
