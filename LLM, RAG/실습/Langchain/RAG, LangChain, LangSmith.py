from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma # from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='key.env')  # 환경변수 파일에서 불러오기
api_key = os.getenv("GROUP_API_KEY")
ls_api_key = os.getenv("LS_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true" # langsmith 환경 구성.
os.environ["LANGCHAIN_API_KEY"] = ls_api_key

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

# 랭체인에는 이미 만들어져있는 여러가지 Loader 들이 존재한다. 
# (PDFLoader, GitLoader, GoogleDriveLoader, NotionDBLoader 등등)
# 그 중에서 WebBaseLoader 는 웹에서 정보를 Load 해오는 Loader
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
)

# loader 는 .load() 라는 일관된 인터페이스를 가지고 있다.
docs = loader.load()

# 다양한 TextSplitter 중 RecursiveCharacterTextSplitter 는
# "\n\n" > "\n" > " " > "" 순서로 텍스트 분할을 시도하는 Splitter
# 아래는 1,000 글자 단위로 split 하되, 200자 까지 겹치는걸 허용한다는 옵션
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# split 된 문서들을 ChromaDB 에 embedding 해서 넣어주는 과정
# ChromaDB 는 대표적인 오픈소스 벡터 데이터베이스 중 하나
# 어떤 임베딩모델을 사용할지, 어떤 문서 조각을 저장할지를 정해준다.
# OpenAIEmbeddings 에 아무 인자도 주지 않으면 "text-embedding-ada-002" 모델이 사용된다
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

'''
# 내가 만든 index 의 이름, 사용할 임베딩 모델, 복사해온 api key 를 넣어준다
# 환경변수에 PINECONE_API_KEY 등록했으면 api_key 는 생략해도 됨
vectorstore = PineconeVectorStore(
    index_name="",
    embedding=OpenAIEmbeddings(),
    pinecone_api_key="",
)

# Pinecone 에 문서를 추가하는 과정, 이 코드가 실행되고 난 뒤 Pinecone 관리 페이지를 다시 들어가보면
# Documents 가 생성된 것을 확인할 수 있다
vectorstore.add_documents(documents=splits)
'''

# 임베딩을 저장한 DB 를 리트리버로 만들기. 
retriever = vectorstore.as_retriever()

# 대표적인 RAG 프롬프트 템플릿을 한국어로 번역한 프롬프트
# 영어 버전으로 사용하는게 LLM 입장에서는 알아듣기 편하나, 성능 낮은 모델의 경우 답변이 영어로 나올 수 있음.
prompt = ChatPromptTemplate.from_template("""
당신은 질문 답변 작업의 보조자입니다.
검색된 다음 문맥을 사용하여 질문에 답하세요.
답을 모른다면 모른다고 말하세요.
답변은 최대 세 문장으로 간결하게 작성하세요.

Question: {question}

Context: {context}

Answer: """)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
)

result = rag_chain.invoke("What is Hallucination?")

print(result)