import cv2
from preprocess import image_encode

def get_image(img_name='test.jpg'):
    # camera 정의
    img = cv2.imread(img_name)

    buffer = image_encode(img)
    # frame을 byte로 변경 후 특정 식??으로 변환 후에 yield로 하나씩 넘겨준다.
    frame = buffer.tobytes()
    yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

def get_video(video_name='test.mp4'): #단일이미지, 영상파일, 실시간영상 단위 옵션을 받아서 수행...
    # camera 정의
    cam = cv2.VideoCapture(video_name)
    while True:
        # 카메라 값 불러오기
        success, frame = cam.read()

        if not success:
            break
        else:
            buffer = image_encode(frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에 yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

def get_stream(camera_info=0):
    # camera 정의
    cam = cv2.VideoCapture(camera_info)

    while True:
        # 카메라 값 불러오기
        success, frame = cam.read()

        if not success:
            break
        else:
            buffer = image_encode(frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에 yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

