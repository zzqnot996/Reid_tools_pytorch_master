import cv2
import os

'''
将视频每隔几帧保存成图片
'''

def extract_frames(video_path, output_folder, frame_interval):

    '''
    video_path : 每个视频的路径 后缀为 ".mp4 或 .avi"
    output_folder : 图片的保留路径 为目录（文件夹）
    frame_interval : 每个几帧保存一下
    '''
    
    cap = cv2.VideoCapture(video_path)  # 打开视频文件
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 获取视频的帧率

    if not os.path.exists(output_folder):  # 确保输出文件夹存在
        os.makedirs(output_folder)

    frame_count = 0  # 逐帧读取视频并保存每隔 frame_interval 帧的帧
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % frame_interval == 0:
            print("the code is running")
            frame_filename = f"frame_{frame_count}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)

    cap.release()  # 释放视频对象
    

 
     


if __name__ == "__main__":

    video_parent_path = r"video"  # 保留视频的文件夹

    for i in os.listdir(video_parent_path):  # 存放所有要分解的视频

        video_path = os.path.join(video_parent_path,i)
        output_folder = os.path.basename(video_path).split(".")[0]  # 取名字
        frame_interval = 3  # 每隔几帧保存一张图片

        extract_frames(video_path, output_folder, frame_interval)    


    print("god, finally done!")


