#!/usr/bin/python3

import re
import subprocess
import cv2
import os

device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb", shell=True)
for i in df.decode().split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            if "045e:0811" in dinfo['id']:
                print("Camera found.")
                bus = dinfo['bus']
                device = dinfo['device']
                break

device_index = None
for file in os.listdir("/sys/class/video4linux"):
    real_file = os.path.realpath("/sys/class/video4linux/" + file)
    print(real_file)
    print("/" + str(bus[-1]) + "-" + str(device[-1]) + "/")
    if "/" + str(bus[-1]) + "-" + str(device[-1]) + "/" in real_file:
        device_index = real_file[-1]
        print("Hurray, device index is =" + str(device_index))


camera = cv2.VideoCapture(int(device_index))

while True:
    (grabbed, frame) = camera.read() # Grab the first frame
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1) & 0xFF
