#!/usr/bin/python3

import re
import os

def get_camera(camera_name):
    cam_num = None
    for file in os.listdir("/sys/class/video4linux"):
        real_file = os.path.realpath("/sys/class/video4linux/" + file + "/name")
        with open(real_file, "rt") as name_file:
            name = name_file.read().rstrip()
        if camera_name in name:
            cam_num = int(re.search("\d+$", file).group(0))
            found = "FOUND!"
            return cam_num
            break
        else:
            found = "      "
        print("{} {} -> {}".format(found, file, name))
    return cam_num

cam_number = get_camera('Microsoft® LifeCam Studio(TM)')
print(cam_number)