import cv2 as cv


def draw_landmarks(image, landmark_point):
    """
    画出对应的关键点与手指框架
    @param image: 传入的视频帧
    @param landmark_point: 手部坐标
    @return: 返回画好的视频帧
    """
    if len(landmark_point) > 0:
        # 大拇指
        Figure_color = (255, 255, 0)
        Finger_circle_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]), Finger_circle_color, 6)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]), Finger_circle_color, 6)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]), Figure_color, 2)

        # 食指
        Index_Finger_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]), Index_Finger_color, 6)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]), Index_Finger_color, 6)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]), Index_Finger_color, 6)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]), Figure_color, 2)

        # 中指
        Middle_Finger_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]), Middle_Finger_color, 6)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]), Middle_Finger_color, 6)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]), Middle_Finger_color, 6)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]), Figure_color, 2)

        # 无名指
        Ring_Finger_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]), Ring_Finger_color, 6)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]), Ring_Finger_color, 6)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]), Ring_Finger_color, 6)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]), Figure_color, 2)

        # 小拇指
        Little_Finger_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]), Little_Finger_color, 6)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]), Little_Finger_color, 6)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]), Figure_color, 2)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]), Little_Finger_color, 6)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]), Figure_color, 2)

        # 手掌
        Palm_color = (255, 191, 0)
        Palm_circle_color = (0, 0, 0)
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]), Palm_color, 2)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]), Palm_circle_color, 6)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]), Palm_color, 2)

    # 手部21个关键点
    key_clolor = (0, 255, 255)  # 淡蓝色
    key_top_color = (101, 238, 101)  # 绿色
    key_circle_color = (0, 0, 0)  # 黑色
    for index, landmark in enumerate(landmark_point):
        if index == 0:  # 手腕
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 1:  # 大拇指 手腕处关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 2:  # 大拇指 第一关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 3:  # 大拇指 第二关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 4:  # 大拇指 指尖 key_top_color
            cv.circle(image, (landmark[0], landmark[1]), 6, key_top_color, -1)
            cv.circle(image, (landmark[0], landmark[1]), 6, key_circle_color, 1)
        if index == 5:  # 食指 第一关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 6:  # 食指 第二关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 7:  # 食指 第三关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 8:  # 食指 指尖 key_top_color
            cv.circle(image, (landmark[0], landmark[1]), 6, key_top_color, -1)
            cv.circle(image, (landmark[0], landmark[1]), 6, key_circle_color, 1)
        if index == 9:  # 中指 第一关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 10:  # 中指 第二关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 11:  # 中指 第三关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 12:  # 中指 指尖 key_top_color
            cv.circle(image, (landmark[0], landmark[1]), 6, key_top_color, -1)
            cv.circle(image, (landmark[0], landmark[1]), 6, key_circle_color, 1)
        if index == 13:  # 无名指 第一关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 14:  # 无名指 第二关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 15:  # 无名指 第三关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 16:  # 无名指 指尖 key_top_color
            cv.circle(image, (landmark[0], landmark[1]), 6, key_top_color, -1)
            cv.circle(image, (landmark[0], landmark[1]), 6, key_circle_color, 1)
        if index == 17:  # 小拇指 第一关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 18:  # 小拇指 第二关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 19:  # 小拇指 第三关节
            cv.circle(image, (landmark[0], landmark[1]), 5, key_clolor, -1)
            cv.circle(image, (landmark[0], landmark[1]), 5, key_circle_color, 1)
        if index == 20:  # 小拇指 指尖 key_top_color
            cv.circle(image, (landmark[0], landmark[1]), 6, key_top_color, -1)
            cv.circle(image, (landmark[0], landmark[1]), 6, key_circle_color, 1)

    return image
