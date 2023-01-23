import cv2
import base64

#단일이미지, 영상파일, 실시간영상 단위 옵션을 받아서 수행...
def get_image(img_name='test.jpg'):
    # camera 정의
    img = cv2.imread(img_name)

    ret, buffer = cv2.imencode('.jpg', img)
    # frame을 byte로 변경 후 특정 식??으로 변환 후에
    # yield로 하나씩 넘겨준다.
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
            ret, buffer = cv2.imencode('.jpg', frame)
            # frame을 byte로 변경 후 특정 식??으로 변환 후에
            # yield로 하나씩 넘겨준다.
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(frame) + b'\r\n')

def get_stream(camera_info=0):
    # camera 정의
    cam = cv2.VideoCapture(camera_info)

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

def img_resize(src, imgsz=(640,640)):
    dst = cv2.resize(src, imgsz)
    return dst

# https://acdongpgm.tistory.com/159
# https://effectivesquid.tistory.com/entry/Base64-%EC%9D%B8%EC%BD%94%EB%94%A9%EC%9D%B4%EB%9E%80
# https://velog.io/@oosiz/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9D%B8%EC%BD%94%EB%94%A9-%EB%94%94%EC%BD%94%EB%94%A9
# https://ballentain.tistory.com/50