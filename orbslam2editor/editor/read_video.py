import csv
import cv2
from django.conf import settings
from django.http import HttpResponse

import os
import base64

class VIDEOFileReader:
    def __init__(self, request_file):
        self.request_file = request_file
        self.file = request_file.FILES['video_file']
        self.video_path = self.file.temporary_file_path()
        self.video_data  = self.read_video_file()
        

    def read_video_file(self):
        if self.request_file.method == 'POST':
            if self.file:
                # video_data = self.file.read()
                # base64_mp4 = base64.b64encode(video_data).decode('utf-8')
                cap = cv2.VideoCapture(self.video_path)
                frames = []
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    _, buffer = cv2.imencode('.jpg', frame)
                    frame_base64 = base64.b64encode(buffer).decode('utf-8')
                    frames.append(frame_base64)

                cap.release()

                print('self.video_path: ', self.video_path)
                print('video_size: ',len(frames))
                return frames
        return None
                


