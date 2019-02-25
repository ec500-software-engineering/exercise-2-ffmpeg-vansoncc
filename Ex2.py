#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import subprocess
import os
import queue
import threading
import json


def con_video():
    video_list = []
    files = os.listdir('./')
    for f in files:
        if f == 'test.mp4':

            # print("Processing", f)

            video_list.append(f)

    # 720p at 2Mbps and 30fps
    # 480p at 1Mbps and 30fps

    subprocess.run('ffmpeg -i %s -s hd720 -r 30 -b:v 2M %s'
                   % (video_list[0], (video_list[0])[:-4] + '720.mp4'),
                   shell=True)
    print ('Processed ' + video_list[0] + 'to hd720')
    subprocess.run('ffmpeg -i %s -s hd480 -r 30 -b:v 1M %s'
                   % (video_list[0], (video_list[0])[:-4] + '480.mp4'),
                   shell=True)
    print ('Processed ' + video_list[0] + 'to hd480')


def main():
    threads = []
    q = queue.Queue()
    try:
        for i in range(1):
            q.put(i)
            t = threading.Thread(target=con_video())
            threads.append(t)

    except Exception as error:
        print(error)

    for thread in threads:
        t.start()
        thread.join()


def ffprobe(file_name):
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    file_name])
    return json.loads(meta)


if __name__ == '__main__':
    main()
