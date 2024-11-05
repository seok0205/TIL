from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")    # API키(환경변수)
)

system_message = {
    "role":"system", "content":"좋은 개발자가 될 수 있을거야"
}

messages = [system_message]

while True:
    user_input = input("사용자 전달:d")
    if user_input == "exit":
        print("즐거운 대화였습니다. 고맙습니다.")
        break

    messages.append({"role":"user","content":user_input})
    completion = client.chat.completions.create(    # ChatGPT API 호출
        model="gpt-4o",   # 호출 모델
        messages=messages
    )

    reply = completion.choices[0].message.content
    print("Answer: " + reply)
    messages.append({"role":"assistant","content":reply})