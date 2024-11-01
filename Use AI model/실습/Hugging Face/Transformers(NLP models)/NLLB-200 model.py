import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

sentence = "The slow green turtle won in the race"

forced_bos_token_id = tokenizer.convert_tokens_to_ids("kor_Hang")

inputs = tokenizer(sentence, return_tensors="pt")

generated_tokens = model.generate(inputs.input_ids, forced_bos_token_id = forced_bos_token_id)

translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

print(f"Translated text: {translated_text}")

'''
Translated text: 느린 녹색 거북이 이 경연에서 승리

M2M100 모델보다 좀 더 정확한 해석값 도출.
'''