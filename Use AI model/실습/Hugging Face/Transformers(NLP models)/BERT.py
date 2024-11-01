import warnings
warnings.filterwarnings('ignore')

from transformers import BertModel, BertTokenizer
import torch
from scipy.spatial.distance import cosine

model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

sentences = [
    "The quick white rabbit jumps over the slow turtles",
    "The quick black fox leaps over the lazy dog"
]

input1 = tokenizer(sentences[0], return_tensors='pt')
input2 = tokenizer(sentences[1], return_tensors='pt')

with torch.no_grad():
    output1 = model(**input1)
    output2 = model(**input2)

embedding1 = output1.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
embedding2 = output2.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

similarity = 1 - cosine(embedding1, embedding2)

print(f"Cosine similarity between the two sentences: {similarity:.4f}")

'''
"The quick white rabbit jumps over the slow turtles"
"the king is Seok"

결과 : Cosine similarity between the two sentences: 0.5920

"The quick white rabbit jumps over the slow turtles"
"The quick black fox leaps over the lazy dog"

결과 : Cosine similarity between the two sentences: 0.8851
'''