from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='key.env')
api_key = os.getenv('GROUP_API_KEY')

# LLM 모델, OpenAI 외에 다른 모델도 유사하게 불러와서 쓰면 된다.
llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

# messages. LLM 에 들어갈 메세지를 넣어준다.
# SystemMessage 는 대화 바깥의 메세지. 시스템에게 명령을 입력해두는 것
# HumanMessage 는 대화에서 인간 측의 메세지
messages = [
    SystemMessage(content="다음을 영어에서 한국어로 번역하세요."),
    HumanMessage(content="Your mouth is too fast."),
]

# StrOutputParser 는 결과물에서 Str(문자열)만 뽑아준다 
parser = StrOutputParser()

# LLM 에 message 를 invoke 하면 결과를 받아볼 수 있다.
result_1 = llm.invoke(messages)
result_2 = parser.invoke(result_1)

print(result_1)
print(result_2)

# invoke 연쇄적 호출하는 경우, LECL로 chaining을 한 다음 한번의 invoke로 처리 가능.
chain = llm | parser
result_3 = chain.invoke(messages)

print(result_3)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [("system", "다음 영어된 문장을 {language}어로 번역하세요."), 
    ("user", "{text}")]
)

# Prompt 에 자리(language, text) 만들어두고 invoke 하면 해당 자리에 들어간다
result_4 = prompt.invoke({"language": "한국", "text": "You are too lazy."})

# invoke 가 되기 때문에 Prompt 도 하나의 Runnable 로 취급되는걸 알 수 있다.
print(result_4)

# prompt, llm, parser 세 개의 Runnable 을 체이닝해서 체인으로 만든 상태
chain_2 = prompt | llm | parser

result_5 = chain_2.invoke({"language": "Korean", "text": "You are too lazy."})

print(result_5)