import cv2
import numpy as np
import math
import datetime
# 创建一个白色的背景图像
image = np.ones((400, 400, 3), dtype=np.uint8)*255


# 画一个黑色的圆，参数 2：圆心坐标，参数 3：半径
cv2.circle(image, (200, 200), 170, (0, 0, 0), 6)
hourline = []
minuteline = [] 
for i in range (60):
    if i % 5 == 0:
        hour_line = np.array([[(200+170*math.cos(math.radians(6*i))), (200+170*math.sin(math.radians(6*i)))],  [(200+140*math.cos(math.radians(6*i))), (200+140*math.sin(math.radians(6*i)))]], np.int32).reshape((-1, 1, 2))
        hourline.append(hour_line)
    else :
        minute_line = np.array([[(200+170*math.cos(math.radians(6*i))), (200+170*math.sin(math.radians(6*i)))],  [(200+155*math.cos(math.radians(6*i))), (200+155*math.sin(math.radians(6*i)))]], np.int32).reshape((-1, 1, 2))
        minuteline .append(minute_line)
    
       
cv2.polylines(image, hourline, True, (0, 0, 0), thickness=6)
cv2.polylines(image, minuteline, True, (0, 0, 0), thickness=3)
while True :
    
    # 画一个填充白色的圆，参数 2：圆心坐标，参数 3：半径，清除指针
    cv2.circle(image, (200, 200), 141, (255, 255, 255), -1)
    #画一个轴点
    cv2.circle(image, (200, 200), 10, (0, 0, 0), -1)
    
    #获取当前日期和时间
    current_datetime = datetime.datetime.now()
    # print(current_datetime)
    current_hour   = current_datetime.hour%12
    current_minute = current_datetime.minute
    current_second = current_datetime.second
    hour_angle = 30 * current_hour + 0.5*current_minute-90
    minute_angle = 6*current_minute + 0.1*current_second-90
    second_angle = 6*current_second-90
    # 添加时间
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'{current_datetime.day}/{current_datetime.month}/{current_datetime.year}', (110, 300), font,
                1, (0, 200, 0), 2, lineType=cv2.LINE_AA)
    
    # 计算秒针、分针和时针的终点坐标 
    second_end = (200 + int(140 * math.cos(math.radians(second_angle))),
                200 + int(140 * math.sin(math.radians(second_angle))))
    minute_end = (200 + int(110 * math.cos(math.radians(minute_angle))),
                200 + int(110 * math.sin(math.radians(minute_angle))))
    hour_end = (200 + int(80 * math.cos(math.radians(hour_angle))),
                200 + int(80 * math.sin(math.radians(hour_angle))))

    # 绘制时针、分针和秒针
    cv2.line(image, (200, 200), hour_end, (255, 0, 255), thickness=6)
    cv2.line(image, (200, 200), minute_end, (255, 255, 0), thickness=3)
    cv2.line(image, (200, 200), second_end, (0, 255, 0), thickness=2)

    
    # 显示图像
    cv2.imshow('OpenCV Clock', image)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
