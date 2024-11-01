import warnings
from transformers import pipeline

warnings.filterwarnings('ignore')

classifier = pipeline("sentiment-analysis", model="roberta-base")

result = classifier("This product is amazing!")
print(result)

# 결과 : [{'label': 'LABEL_0', 'score': 0.5832896828651428}]