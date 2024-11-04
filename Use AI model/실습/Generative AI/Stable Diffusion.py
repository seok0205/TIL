from diffusers import StableDiffusionPipeline
import torch

# Stable Diffusion 파이프라인 로드
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)  # 모델이 사용하는 데이터 유형. GPU 사용 시 float16이 성능에 유리.
pipe = pipe.to("cuda")  # GPU 사용

# prompt는 생성할 이미지의 내용을 설명하는 텍스트.
prompt = "A futuristic cityscape with flying cars at sunset"
image = pipe(prompt).images[0]

'''
image = pipe(prompt, guidance_scale=7.5, num_inference_steps=50).images[0]
guidance_scale은 텍스트 조건을 얼마나 강하게 반영할지 결정하는 파라미터.
num_inference_steps은 이미지 생성 과정에서의 추론 단계 수. 단계수 많을수록 이미지 품질 향상, 생성 시간 증가.
'''

image.show()