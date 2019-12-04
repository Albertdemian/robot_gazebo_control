#!/usr/bin/env python
# license removed for brevity

import unittest
import rospy
from std_msgs.msg import Float64
from time import sleep
import rostest

class publishermsg_test(unittest.TestCase):
    publisher_working = False

    def callback(self,data):
        self.publisher_working = True
    
    def test_publisher(self):
        rospy.init_node('publisher_test')
        rospy.Subscriber('/continuum/joint1_position_controller/command',Float64, self.callback)

        counter = 0
        while not rospy.is_shutdown() and counter < 5 and (not self.publisher_working):
            sleep(5)
            counter +=1 

        self.assertTrue(self.publisher_working)


if __name__ == '__main__':
    rostest.rosrun('testing', 'publisher_test', publishermsg_test)