#!/usr/bin/python3

import re
import os
from os import path

def get_camera(camera_name):
    cam_num = None
    for file in os.listdir("/sys/class/video4linux"):
        if not path.exists("/sys/class/video4linux/" + file + "/device/input/"):
            continue
        input_name = os.listdir("/sys/class/video4linux/" + file + "/device/input/")
        real_file = os.path.join("/sys/class/video4linux/" + file + "/device/input/"+ input_name[0] + "/name")
        with open(real_file, "rt") as name_file:
            name = name_file.read().rstrip()
            print(name + ' -- Video Channel -- ' + file[-1])
        if camera_name in name:
            port_return = file[-1]
            return port_return
            break
        else:
            found = ""


cam_number = get_camera('xxx')
