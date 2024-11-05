from ultralytics import YOLO
import cv2
from matplotlib import pyplot as plt

# YOLOv8 모델 로드 (YOLOv8s)
model = YOLO('yolov8n.pt')

# 웹캠을 통해 실시간 객체 탐지
cap = cv2.VideoCapture(0)  # 웹캠 캡처 시작

# 웹캠 -> 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임을 YOLOv8 모델에 입력하여 객체 탐지 수행
    results = model(frame)
	
    # 탐지 객체 프레임에 그리기
    annotated_frame = results[0].plot() # 모델이 객체 탐지한 결과 반환
	
    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)
  
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()