import warnings
warnings.filterwarnings('ignore')

from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

sentence = "The slow green turtle won in the race"

encoded_sentence = tokenizer(sentence, return_tensors="pt")

tokenizer.src_lang = "en"
model.config.forced_bos_token_id = tokenizer.get_lang_id("ko")

generated_tokens = model.generate(**encoded_sentence)

translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

print(f"Translated text: {translated_text}")

# Translated text: 천천히 녹색 거북이가 경주에서 승리했다.