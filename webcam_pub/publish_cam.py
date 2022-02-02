#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image
from pygrabber.dshow_graph import FilterGraph
import matplotlib.pyplot as plt
import cv2
import numpy as np
import re
import os


class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image,'/Webcam',10)
        timer_period = 1/60; #camera runs with 60 FPS
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        cam_number = self.get_camera('Microsoft® LifeCam Studio(TM)')

        self.cap = cv2.VideoCapture(cam_number)
 
        self.cvBridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        msg = self.cvBridge.cv2_to_imgmsg(frame)

        
        msg.header.frame_id = '1'

        if ret:
            self.publisher_.publish(msg)
    
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
        

def main(args=None):
    
    rclpy.init(args=args)

    video_publisher = VideoPublisher()

    rclpy.spin(video_publisher)

    video_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main() 

        
