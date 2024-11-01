import warnings
from transformers import pipeline

warnings.filterwarnings('ignore')

generator = pipeline("text-generation", model="gpt2")

result = generator("I love rock music", max_length=50, num_return_sequences=1)

print(result)

'''
결과:[{'generated_text': 'I love rock music so you can experience it to its fullest (and the music will continue to grow), but all the best is still missing out on making friends, you know? Even if you decide 
to stay outside all day, but we all did'}]
'''
