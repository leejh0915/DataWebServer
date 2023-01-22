import cv2

def get_stream_video(): #단일이미지, 영상파일, 실시간영상 단위 옵션을 받아서 수행...
    # camera 정의
    cam = cv2.VideoCapture('test.mp4')

    while True:
        # 카메라 값 불러오기
        success, frame = cam.read()

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(frame) + b'\r\n')

def image_decode(src):
    dst = src
    return dst

def image_encode(src):
    dst = src
    return dst

def img_resize(src):
    dst = src
    return dst

# https://acdongpgm.tistory.com/159
# https://effectivesquid.tistory.com/entry/Base64-%EC%9D%B8%EC%BD%94%EB%94%A9%EC%9D%B4%EB%9E%80
# https://velog.io/@oosiz/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9D%B8%EC%BD%94%EB%94%A9-%EB%94%94%EC%BD%94%EB%94%A9
# https://ballentain.tistory.com/50