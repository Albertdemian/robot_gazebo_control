#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math 
import time

t_end = time.time()+ 30

def talker():
    pub1 = rospy.Publisher('/continuum/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/continuum/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/continuum/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/continuum/joint4_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(50) # 10hz
    while not rospy.is_shutdown():
#        while time.time() < t_end:
            t = time.time()
            angle1 = math.sin(t)/5
            angle2 = math.sin(t)/5
            #angle2 = 0
            angle3 = math.sin(t)/5
            angle4 = math.sin(t)/5
            #angle4 = 0
            hello_str = "hello world  %f" % angle1
            rospy.loginfo(hello_str)
            pub1.publish(angle1)
            pub2.publish(angle2)
            pub3.publish(angle3)
            pub4.publish(angle4)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
        
    except rospy.ROSInterruptException:
        pass
