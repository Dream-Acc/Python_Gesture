import cv2


def draw_rect_txt(frame, info_text, brect):
    """
    输出识别结果在矩阵上方
    @param frame: 每一帧图片
    @param info_text: 要显示的文本
    @param brect: 显示的位置
    """
    cv2.putText(frame, info_text, (brect[0] + 5, brect[1] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1,
                cv2.LINE_AA)
