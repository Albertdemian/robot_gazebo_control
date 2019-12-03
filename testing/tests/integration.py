#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from sensor_msgs.msg import JointState
from time import sleep
import unittest
import rostest
import numpy as np
from numpy import testing
import time


class integration_test(unittest.TestCase):
    state = 0
    command = 0
    angle1 = 0.0
    def callback_msg(self,data):
        
        self.state = data.position
        print(self.state[0], type(self.state[0]))

    def callback_real(self,data):
        
        self.command = data 
        print(self.command, type(self.command))

    def test_listener(self):
        t_end = time.time()+ 10

        rospy.init_node('joint_state_sub', anonymous=True)
    
        pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
        
        while time.time() < t_end:
            t = time.time()
            pub1.publish(self.angle1)

        
        rospy.Subscriber("/rrbot/joint_states", JointState, self.callback_msg)
        sleep(1)

        
        a = self.state[0]
        
        self.assertAlmostEqual(self.angle1,a,2)
        

if __name__ == '__main__':
    rostest.rosrun('testing', 'joint_state_sub', integration_test)
    