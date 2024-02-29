# Reid_tools_pytorch_master

## video_pic_tools

### extract_frames_from_video.py

'''
将视频每隔几帧保存成图片
'''

def extract_frames(video_path, output_folder, frame_interval):

    '''
    video_path : 每个视频的路径 后缀为 ".mp4 或 .avi"
    output_folder : 图片的保留路径 为目录（文件夹）
    frame_interval : 每个几帧保存一下
    '''
