#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from sensor_msgs.msg import JointState
def callback(data):
    rospy.loginfo( data.position)
    print(data.position)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_state_sub', anonymous=True)

    rospy.Subscriber("/rrbot/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()