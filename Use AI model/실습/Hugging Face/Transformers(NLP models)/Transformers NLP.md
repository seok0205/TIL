# Hugging Face의 Transformers 라이브러리(NLP 모델)

## Transformers 라이브러리

- 다양한 NLP 모델을 쉽게 사용할 수 있도록 도와주는 Hugging Face의 오픈소스 라이브러리다. 최신 NLP 모델들을 불러와 텍스트 생성, 감정 분석, 번역 등 다양한 작업에 활용할 수 있음.  

### GPT-2 (Generative Pre-trained Transformer 2)  

- OpenAI에서 개발한 언어 생성 모델, 문장을 생성하거나 이어지는 텍스트를 예측하는 데 뛰어난 성능 발휘.  

### 간단한 감정 분석(Sentiment Analysis)  

- 이 파이프라인은 텍스트 데이터를 입력으로 받아 그 텍스트의 감정을 분석하는 작업을 수행. 주로 긍정, 부정, 중립을 판단함.  

### RoBERTa (Robustly Optimized BERT Approach)  

- BERT 모델을 최적화한 버전. 더 많은 데이터와 더 긴 학습 시간을 통해 성능을 향상시킴. 텍스트 분류와 감정 분석 같은 작업에서 뛰어난 성능을 자랑함.  

#### 정확히 안나오는 이유  

- BERT는 Google에서 개발한 NLP모델, 문맥을 양방향으로 이해하는 능력을 가짐. Hugging Face의 대표 모델 중 하나. BERT는 기본적으로 사전 학습만 되어 있어서 텍스트 분류와 같은 작업에 사용하려면 미세조정(Fine-Tuning)이 필요. 그렇지 않으면 정상적 작동을 하지 않을 수 있음.  
- Fine-Tuning을 통해 분류 레이어의 가중치를 학습시키지 않으면 모델이 적절한 예측 하기가 힘듦. 따라서 BERT 사용하려면, 사용자가 제공하는 데이터에 맞춰 추가 학습이 필요함.  
