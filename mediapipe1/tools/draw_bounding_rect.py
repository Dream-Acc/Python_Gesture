import numpy as np
import cv2


def draw_bounding_rect(image, landmarks_point):
    """
    画出手对应的矩形
    @param image: 传入的视频帧
    @param landmarks_point: 手部关键点坐标
    @return: 已加入对应矩形的视频帧
    """
    # cv2.boundingRect 获得图像的最小矩形边框一些信息
    x, y, w, h = cv2.boundingRect(np.array(landmarks_point))
    # brect 矩形四个点坐标
    brect = [x, y, x + w, y + h]
    # cv2.rectangle 画出该最小边框
    cv2.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]), (0, 0, 0), 1)

    return brect
