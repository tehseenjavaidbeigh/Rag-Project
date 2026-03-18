from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
data = PyPDFLoader("documents_loader/dataset.pdf")
docs = data.load()
model = ChatMistralAI(model = "mistral-small-2506")
template =ChatPromptTemplate.from_messages(
    [("system","You are an AI that summarises the text"),
     ("human","{data}")])

prompt = template.format_messages(data = docs[0].page_content)

result = model.invoke(prompt)
print(result.content)
#unlike text file pdf will not have length of 1
