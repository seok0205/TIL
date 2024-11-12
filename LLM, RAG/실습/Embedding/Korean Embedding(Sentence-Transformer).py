'''
문장 단위로 임베딩을 생성할 수 있는 BERT 기반의 모델.
특히 한국어에 특화된 Ko-Sentence-BERT 같은 모델을 사용하면, 문장 간의 의미적 유사성을 정확히 계산 가능.
'''

from sentence_transformers import SentenceTransformer
import numpy as np

# Multilingual-E5-large-instruct 모델 로드
model = SentenceTransformer('intfloat/multilingual-e5-large')

# 'sentence-transformers/kr-sentence_bert-base' 최신 Ko-Sentence-BERT 모델

# 문장 리스트
sentences = [
    "부산에서 서면은 유명한 장소입니다.",
    "광안리나 해운대를 가면 아름다운 장관을 볼 수 있습니다.",
    "겨울을 대비해 스키 타는 법을 배워봅시다.",
    "초보자가 타기 좋은 스키와 입기 좋은 스키복 고르는 방법을 알아보겠습니다.",
    "스키장 가실 분들은 모두 엉덩이를 조심하세요!"
]

# 문장들을 임베딩으로 변환
embeddings = model.encode(sentences)

# 임베딩 벡터 출력
print(embeddings.shape)  # (5, 1024) - 5개의 문장이 1024 차원의 벡터로 변환됨

'''
특징  
장점 : 문장 간의 유사성을 정확히 측정, 문맥을 고려한 임베딩 생성.
단점 : 학습 속도가 상대적으로 느림.
'''