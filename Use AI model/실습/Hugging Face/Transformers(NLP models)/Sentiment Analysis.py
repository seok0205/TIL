import warnings
from transformers import pipeline

warnings.filterwarnings('ignore')

sentiment_analysis = pipeline("sentiment-analysis")
result = sentiment_analysis("This movie is the greatest the world has ever seen!")
print(result)

# 결과 : [{'label': 'POSITIVE', 'score': 0.999849796295166}]