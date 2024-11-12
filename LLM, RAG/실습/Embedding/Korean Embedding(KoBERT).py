'''
BERT, GPT 같은 모델들로 발전, 최근 KoBERT, KoGPT 같은 한국어 특화 모델 등장.
문맥을 고려해 정교한 임베딩 생성.
'''

from transformers import BertTokenizer, BertModel
import torch

# KLUE-BERT 모델과 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('klue/bert-base')
model = BertModel.from_pretrained('klue/bert-base')

# 입력 문장
sentence = "세상에서 가장 축구를 잘하는 사람은 손흥민이다."

# 토큰화 및 텐서 변환
inputs = tokenizer(sentence, return_tensors='pt')

# 임베딩 생성
with torch.no_grad():
    outputs = model(**inputs)

# 임베딩 벡터 추출 (평균값으로 계산)
embedding = outputs.last_hidden_state.mean(dim=1)
print(embedding)

'''
특징
장점 : 문맥을 양방향으로 이해, 문장 전체의 의미를 깊이 반영.
단점 : 계산 비용이 크고, 모델 크기가 큼.
'''