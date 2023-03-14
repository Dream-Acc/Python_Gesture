import cv2
import mediapipe as mp
import numpy as np
from tools.landmark_handle import landmark_handle

video_num = 1
# 手语集
label = ["bad", "birthday", "good", "he", "help", "home", "introduce", "late", "me", "meet",
         "name", "sit", "sorry", "today", "yesterday", "you"]
label_num = len(label)
print("label_num:" + str(label_num))
# 模型保存地址即是label+.npz
# video_path即是label+_

# 手部模型定义
# mp.solutions.drawing_utils 将识别到的手部关键点信息绘制道cv2图像中
mp_drawing = mp.solutions.drawing_utils
# mp.solutions.hands 将手分成21个点
mp_hands = mp.solutions.hands
# mp_hands.Hands 初始化手部识别类
hands = mp_hands.Hands(
    static_image_mode=False,  # 静态图像还是连续帧视频 False连续帧视频 True静态图像
    max_num_hands=1,  # 最多识别多少只手
    min_detection_confidence=0.5,  # 检测置信度阈值
    min_tracking_confidence=0.5)  # 各帧之间跟踪置信度阈值

for i in range(label_num):
    print(str(i + 1) + "/" + str(len(label)) + ":" + label[i])
    data = []
    for j in range(video_num):
        cap = cv2.VideoCapture("./Video/static/" + label[i]+".mp4")
        # cap.read()
        # 参数ret 为True 或者False,代表有没有读取到图片
        # 第二个参数frame表示截取到一帧的图片
        ret, frame = cap.read()
        while ret is True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # cv2.flip 使图像进行翻转
            frame = cv2.flip(frame, 1)
            # hands.process完成对图像的处理
            # 如果检测到手，那么将返回一个列表，包含21个标志点的x、y、z的值
            results = hands.process(frame)
            # 将RGB图片变为BGR图片
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    hand_local = []
                    for ix in range(21):
                        x = min(int(hand_landmarks.landmark[ix].x * frame.shape[1]), frame.shape[1] - 1)
                        y = min(int(hand_landmarks.landmark[ix].y * frame.shape[0]), frame.shape[0] - 1)
                        hand_local.append([x, y])
                    hand_local = landmark_handle(hand_local)
                    data.append(hand_local)

            ret, frame = cap.read()

    # 保存制作好的npz数据
    np.savez_compressed("./npz_files/" + label[i] + ".npz", data=data)
