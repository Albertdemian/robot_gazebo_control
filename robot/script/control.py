#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math 
import time

t_end = time.time()+ 30

def talker():
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/rrbot/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/rrbot/joint4_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        while time.time() < t_end:
            t = time.time()
            angle1 = math.sin(t)/10
            angle2 = math.cos(t)/10
            angle3 = math.sin(t)/10
            angle4 = math.cos(t)/10
            hello_str = "hello world %s" % rospy.get_time()
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
