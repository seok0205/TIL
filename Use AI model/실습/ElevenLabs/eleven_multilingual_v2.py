import os
import requests
from pydub import AudioSegment
import io
from dotenv import load_dotenv

load_dotenv(dotenv_path='Use AI model\실습\ElevenLabs\seok.env')    # 환경변수에 저장한 api, url 불러오기.(보안)

api_key = os.getenv("API_KEY")
url = os.getenv("API_URL")

# 설정 가능한 변수
output_filename = "output_audio.mp3"

headers = {
    "xi-api-key":api_key,
    "Content-Type":"application/json"
}

# 문장을 입력받습니다.
text = input("텍스트를 입력하세요:")

# 음성 생성 요청을 보냅니다.
data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 1,
        "style": 1,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=data, headers=headers, stream=True)

if response.status_code == 200:
    audio_content = b""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_content += chunk

    current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉토리 경로
    output_path = os.path.join(current_dir, "output_audio.mp3") # outputaudio 파일 경로 생성

    segment = AudioSegment.from_mp3(io.BytesIO(audio_content))
    segment.export(output_path, format="mp3")   # 생성 파일 지정 경로에 저장.
    print(f"Success! Wrote audio to {output_filename}")

else:
    print(f"Failed to save file: {response.status_code}")