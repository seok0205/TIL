'''
단어를 고차원 벡터로 변환해 의미적 유사성을 측정하는 임베딩 기법.
단어 간 문맥적 관계를 반영, 비슷한 의미를 가진 단어들이 유사한 벡터 값을 갖도록 학습.
'''

from gensim.models import Word2Vec

# 샘플 한국어 문장 데이터
sentences = [
    "손흥민은 토트넘의 선수이다.",
    "토트넘이 경쟁 팀인 아스날에게 승리했다.",
    "축구는 정말 재미있지만 힘든 스포츠이다.",
    "영국의 명문 축구 팀은 참 많다.",
    "토트넘의 상징은 공 위에 올라간 닭이다."
]

# Python 기본 split() 사용해 간단하게 토큰화
tokenized_sentences = [sentence.split() for sentence in sentences]

# Word2Vec 모델 학습
word2vec_model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# 단어 '고양이'와 유사한 단어 찾기
similar_words = word2vec_model.wv.most_similar("축구")
print(similar_words)

"""
특징 :  
장점 : 단어 간의 의미적 관계 파악에 적합
단점 : 단어 자체만 학습, 문장 단위에서는 유연성 부족
"""