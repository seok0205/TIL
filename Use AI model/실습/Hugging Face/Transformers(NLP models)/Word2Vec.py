import warnings
warnings.filterwarnings('ignore')

from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from scipy.spatial.distance import cosine
import numpy as np

sentences = [
    "Man is good at to use strength",
    "Woman is delicate",
    "A man is moving a heavy box",
    "A woman is reading a novel",
]

processed = [simple_preprocess(sentence) for sentence in sentences]
print(processed)

model = Word2Vec(sentences = processed, vector_size= 5, window = 5, min_count = 1, sg = 0)
man = model.wv['man']
woman = model.wv['woman']

sim = 1 - cosine(man, woman)
print(sim)

'''
[['man', 'is', 'good', 'at', 'to', 'use', 'strength'], ['woman', 'is', 'delicate'], ['man', 'is', 'moving', 'heavy', 'box'], ['woman', 'is', 'reading', 'novel']]
-0.6736044139498998
'''