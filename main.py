# StreamingResponse를 가져와야함
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

import uvicorn
from webdata import get_stream

# FastAPI 인스턴스 생성
app = FastAPI()

# 스트리밍 경로를 /video 경로로 설정.
@app.get("/video")
def video():
    # StringResponse함수를 return하고,
    # 인자로 OpenCV에서 가져온 "바이트"이미지와 type을 명시
    return StreamingResponse(get_stream(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=2121)