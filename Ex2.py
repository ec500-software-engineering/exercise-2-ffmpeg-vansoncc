#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
import queue
import threading
import json
from pathlib import Path



def con_video():
    video_list = []
    files = os.listdir('./')
    for f in files:
        if f == 'test.mp4':
            # print("Processing", f)

            video_list.append(f)

    # 720p at 2Mbps and 30fps
    # 480p at 1Mbps and 30fps

    return video_list


def con_720():
    filename = con_video()
    subprocess.run('ffmpeg -i %s -s hd720 -r 30 -b:v 2M %s'
                   % (filename[0], (filename[0])[:-4] + '720.mp4'),
                   shell=True)
    print('Processed ' + filename[0] + ' to hd720')


def con_480():
    filename = con_video()
    subprocess.run('ffmpeg -i %s -s hd480 -r 30 -b:v 1M %s'
                   % (filename[0], (filename[0])[:-4] + '480.mp4'),
                   shell=True)
    print('Processed ' + filename[0] + ' to hd480')


def main(n):
    threads = []
    q = queue.Queue()
    i = 1
    try:
        for i in range(n):
            q.put(i)
            t1 = threading.Thread(target=con_720())
            t2 = threading.Thread(target=con_480())
            threads.append(t1)
            threads.append(t2)
            t1.start()
            t2.start()

    except Exception as error:
        print(error)

    for thread in threads:

        thread.join()


# def ffprobe_sync(filein: Path) -> dict:
#         """ get media metadata """
#     meta_json = subprocess.check_output([
#         'ffprobe', '-v', 'warning', '-print_format',
#         'json', '-show_streams', '-show_format', filein],
#         universal_newlines=True)
#
#     return json.loads(meta_json)



if __name__ == '__main__':
    main(2)
