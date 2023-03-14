import os
import cv2
import mediapipe as mp
import torch as t
from ..model.model import HandModel
from ..model.tools.landmark_handle import landmark_handle
from ..model.tools.draw_landmarks import draw_landmarks
from ..model.tools.draw_bounding_rect import draw_bounding_rect
import time
import tkinter as tk


def use_model(purpose_label):
    root = tk.Tk()
    center_x = root.winfo_screenwidth() // 2
    center_y = root.winfo_screenheight() // 2
    print("start")
    lst = [0 for _ in range(16)]
    basis = os.getcwd()
    model_path = basis + '\\gesture\\model\\checkpoints\\model_39.pth'
    # 手语集
    label = ["bad", "birthday", "good", "he", "help", "home", "introduce", "late", "me", "meet",
             "name", "sit", "sorry", "today", "yesterday", "you"]
    # label_num 标签数量
    label_num = len(label)
    number = -1
    for i in range(16):
        if label[i] == purpose_label:
            number = i
            break

    # 识别模型定义
    model = HandModel()
    state_dict = t.load(model_path)
    # load_state_dict 用于将预训练的参数权重加载到新的模型之中
    model.load_state_dict(state_dict)

    # 手部模型定义
    # mp.solutions.hands 将手分成21个点
    mp_hands = mp.solutions.hands
    # mp_hands.Hands 初始化手部识别类
    hands = mp_hands.Hands(
        static_image_mode=False,  # 静态图像还是连续帧视频 False连续帧视频 True静态图像
        max_num_hands=1,  # 最多识别多少只手
        min_detection_confidence=0.75,  # 检测置信度阈值
        min_tracking_confidence=0.75)  # 各帧之间跟踪置信度阈值
    cap = cv2.VideoCapture(0)  # 从摄像机中读取视频

    print(label[number])
    i = 0
    # 共检测10s
    while i <= 20:
        i = i + 1
        time.sleep(0.5)
        # cap.read()
        # 参数ret 为True 或者False,代表有没有读取到图片
        # 第二个参数frame表示截取到一帧的图片
        ret, frame = cap.read()
        # 将BGR图片变为RGB图片
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # cv2.flip 使图像进行翻转
        frame = cv2.flip(frame, 1)
        # hands.process完成对图像的处理
        # 如果检测到手，那么将返回一个列表，包含21个标志点的x、y、z的值
        results = hands.process(frame)
        # 将RGB图片变为BGR图片
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        hand_local = []
        # multi_hand_landmarks 被检测 / 跟踪的手的集合，其中每只手被表示为21个手部地标的列表
        # 如果为真 即为被检测到
        if results.multi_hand_landmarks:
            # hand_landmarks为每一个手部模型
            for hand_landmarks in results.multi_hand_landmarks:
                # 画出对应的21个坐标
                for i in range(21):
                    x = min(
                        int(hand_landmarks.landmark[i].x * frame.shape[1]), frame.shape[1] - 1)
                    y = min(
                        int(hand_landmarks.landmark[i].y * frame.shape[0]), frame.shape[0] - 1)
                    hand_local.append([x, y])
                # 自己填骨架的色
                draw_landmarks(frame, hand_local)
                brect = draw_bounding_rect(frame, hand_local)
                # brect是框架的四个点坐标
                hand_local = landmark_handle(hand_local)

        # 识别部分
        if hand_local:
            # 模型输入为hand_local 输出为分类结果
            output = model(t.tensor(hand_local))
            index, value = output.topk(1)[1][0], output.topk(1)[0][0]
            lst[index] = lst[index] + 1
            this_label = label[index]
            # 输出当前的识别结果
            cv2.putText(frame, this_label, (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

        # 识别窗口名称
        x = int(650)
        y = int(500)
        cv2.namedWindow('MediaPipe Hands', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('MediaPipe Hands', x, y)
        cv2.moveWindow("MediaPipe Hands", center_x -
                       int(x * 0.5), center_y - int(y * 0.5))
        cv2.imshow('MediaPipe Hands', frame)
        #  waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
        if cv2.waitKey(1) & 0xFF == 27:
            break

    print("end")
    cv2.destroyAllWindows()
    cap.release()
    if lst[number] >= 2:
        print("True")
        return True
    else:
        print("False")
        return False
